from django.shortcuts import render
from django.views.generic import(
		ListView,
		DetailView,
		CreateView,
		UpdateView,
		DeleteView
	)
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Blog,Notice

# Create your views here.
class BlogCreateView(LoginRequiredMixin,CreateView):
	model=Blog
	fields=['title','content','image']

	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)

class BlogListView(ListView):
	model=Blog
	context_object_name='blogs'
	ordering=['-date_posted']

class BlogDetailView(DetailView):
	model=Blog
	context_object_name='blog'
	template_name='blog/blog-single.html'
class BlogUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model=Blog
	fields=['title','content','image']

	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)

	def test_func(self):
		post=self.get_object()
		if self.request.user == post.author:
			return True
		return False
class NoticeCreateView(LoginRequiredMixin,CreateView):
	model=Notice
	fields=['title','content']
	template_name='notice/notice-create.html'

	def form_valid(self,form):
		form.instance.user=self.request.user
		return super().form_valid(form)

class NoticeListView(ListView):
	model=Notice
	context_object_name='notices'
	template_name='notice/notice-list.html'
	ordering=['-date_posted']
class NoticeDetailView(DetailView):
	model=Notice
	context_object_name='notice'
	template_name='notice/notice-detail.html'
class NoticeUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model=Notice
	fields=['title','content']
	template_name='notice/notice-create.html'
	def form_valid(self,form):
		form.instance.user=self.request.user
		return super().form_valid(form)

	def test_func(self):
		# post=self.get_object()
		if self.request.user.username == 'admin':
			return True
		return False