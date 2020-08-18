from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .forms import Books
# Create your views here.
from django.views.generic import (
		ListView,
		DetailView,
		CreateView,
		UpdateView,
		DeleteView

	)
from django.http import HttpResponse
from .models import Book,Book_Specification,booked
from django.contrib.messages.views import SuccessMessageMixin

class BookCreateView(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,CreateView):
	model=Book
	template_name='library/book_create.html'
	success_message = "Book was added to present list"
	# context_object_name='student'
	fields=['name','total_quantity','edition','writer','subject','remaining_quantity']
	def form_valid(self,form):
		# form.instance.user=self.request.user
		print(form.cleaned_data)
		return super().form_valid(form)
	def test_func(self):
		if self.request.user.username=='admin':
			return True
		else:
			return False

class Book_SpecificationCreateView(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,CreateView):
	model=Book_Specification
	template_name='library/book_create.html'
	# context_object_name='student'
	success_message = "Book was given"
	fields=['book','book_number','teacherinfo','date_issue','date_return']
	def form_valid(self,form):
		# form.instance.user=self.request.user
		print(form.cleaned_data)
		return super().form_valid(form)
	def test_func(self):
		if self.request.user.username=='admin':
			return True
		else:
			return False

class BookListView(LoginRequiredMixin,ListView):
	model=Book
	template_name='library/book_list.html'
	context_object_name='books'

class BookDetailView(LoginRequiredMixin,SuccessMessageMixin,DetailView):
	model=Book_Specification
	template_name='library/books_detail.html'
	context_object_name='book'
	def form_valid(self,form):
		# form.instance.user=self.request.user
		print(form.cleaned_data)
		return super().form_valid(form)


def bookdetailview(request,pk):
	bookobj=Book.objects.get(id=pk)

	# bookobject=Book.objects.get(book=bookobj)
	if request.method=='POST':
		form=Books(request.POST)
		if form.is_valid():
			# book_specification=form.cleaned_data['book_specification']
			# teacherinfo=form.cleaned_data['teacherinfo']
			# studentinfo=form.cleaned_data['studentinfo']
			date_issue=form.cleaned_data['date_issue']
			date_return=form.cleaned_data['date_return']
			# a=booked(book_specification=book_specification,teacherinfo=teacherinfo,studentinfo=studentinfo,date_issue=date_issue,date_return=date_return)
			form.save()
			# total_quantity=bookobj.total_quantity-1
			if date_issue:
				remaining_quantity=bookobj.remaining_quantity-1
				bookobj.remaining_quantity=remaining_quantity
				bookobj.save(update_fields=['remaining_quantity'])
			elif date_return:
				remaining_quantity=bookobj.remaining_quantity+1
				bookobj.remaining_quantity=remaining_quantity
				bookobj.save(update_fields=['remaining_quantity'])

			return HttpResponse('/success/')
	else:
		form=Books()
	return render(request,'library/book_detail.html',{"form":form})
# def BookReturnView(request,pk):
