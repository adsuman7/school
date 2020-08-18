from django.shortcuts import render
from .forms import TeacherInfoForm,TeacherUpdateForm,Feepayment
from .models import Teacherinfo,Attendence,Teacher_Payment_Bill,Teacher_Subject
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from datetime import date 
from django.template.loader import get_template
from school.utils import render_to_pdf
from django.urls import reverse
from django.core.mail import send_mail
# from school.settings import EMAIL_HOST_USER
from django.conf import settings

# Create your views here.
from django.views.generic import (
		ListView,
		DetailView,
		CreateView,
		UpdateView,
		DeleteView

	)
from django.views import View
class IndexView(View):

	def get(self, request):
		return render(request,'teacher/index.html')
class TeacherCreateView(LoginRequiredMixin,CreateView):
	model=Teacherinfo
	form_class=TeacherInfoForm
	template_name='teacher/teacher_info_create.html'
	success_url=''
	def form_valid(self,form):
		form.instance.user=self.request.user
		form.instance.user_id=self.request.user.id
		print(form.cleaned_data)
		return super().form_valid(form)

class TeacherListView(LoginRequiredMixin,ListView):
	model=Teacherinfo
	template_name='teacher/teacher.html'
	context_object_name='teachers'

class TeacherDetailView(LoginRequiredMixin,UserPassesTestMixin,DetailView):
	model=Teacherinfo
	template_name='teacher/teacher_info.html'
	context_object_name='teacher'
	def form_valid(self,form):
		form.instance.user=self.request.user
		print(form.cleaned_data)
		return super().form_valid(form)
	def test_func(self):
		teacher=self.get_object()
		if self.request.user==teacher.user:
			return True
		else:
			return False
class TeacherUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model=Teacherinfo
	form_class=TeacherUpdateForm
	template_name='teacher/teacher_info_create.html'
	success_url=''
	def form_valid(self,form):
		form.instance.user=self.request.user
		print(form.cleaned_data)
		return super().form_valid(form)
	def test_func(self):
		teacher=self.get_object()
		if self.request.user==teacher.user:
			return True
		else:
			return False
class TeacherAttendenceView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
	model=Attendence
	# form_class=Teacher_Attendence_Form
	template_name='teacher/teacher_attendence_form.html'
	# success_url='teacher-attendence'
	success_message = "%(calculated_field)s was added to present list"
	fields=['teacherinfo','attendence']
	def form_valid(self,form):
		# form.instance.user=self.request.user
		# form.instance.user_id=self.request.user.id
		print(form.cleaned_data)
		return super().form_valid(form)
	def get_success_message(self, cleaned_data):

		return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.teacherinfo,
        )	
class TeacherSalaryView(LoginRequiredMixin,View):
	def get(self,request,pk,*args,**kwargs):
		context=Teacherinfo.objects.get(id=pk)

		# date_join=context.date_join
		due=int(context.due)
			#context=int(context.fees) + 200
		today = date.today()
		t=today-context.salarypay_date
		month=int(abs(t.days)/30)
		fees=month*int(context.salary)+due

		form=Feepayment()
		pay_date=context.salarypay_date
		context={"form":form,"fees":fees,"pay_date":pay_date}
		return render(request,'teacher/teacher_salary.html',context)
	
	def post(self,request,pk,*args,**kwargs):
		context=Teacherinfo.objects.get(id=pk)
		# date_join=context.date_join
		due=int(context.due)
		pk=int(pk)	#context=int(context.fees) + 200
		today = date.today()
		t=today-context.salarypay_date
		month=int(abs(t.days)/30)
		fees=month*int(context.salary)+due
		
		form=Feepayment(request.POST)
		if form.is_valid():
			given=int(form.cleaned_data['given'])
			name=form.cleaned_data['bill_payer_name']
			due=fees-given
			context.due=due
			context.salarypay_date=today
			context.save(update_fields=['salarypay_date','due'])
			bill=Teacher_Payment_Bill(teacherinfo=context,bill_payer_name=name,paid_amount=given,due_amount=due)
			bill.save()
			subject = 'salary status'
			message = ' your salary has been withdraw please check you account '
			email_from = settings.EMAIL_HOST_USER
			recipient_list = ['adsuman7@gmail.com',]
			send_mail( subject, message, email_from, recipient_list,fail_silently=False,)
			# send_mail(
   #  			'Subject here',
   #  			'Here is the message.',
   #  			EMAIL_HOST_USER,
   #  			['adsuman7@gmail.com'],
   #  			fail_silently=False,
			# )
			# return HttpResponse("ALMOST THERE")
			# return f"salary/pdf/{pk}"
			# return reverse()
			return HttpResponseRedirect(reverse('salary-pdf',kwargs={"pk":pk}))
			

class GeneratePDF(View):
    def get(self,request,pk,*args, **kwargs):
        template = get_template('pdf/invoice.html')
        contexts=Teacherinfo.objects.get(id=pk)
        bill=Teacher_Payment_Bill.objects.filter(teacherinfo=contexts).order_by('-id')[0]
        #bill=s.objects.order_by('paid_date').first()
        context = {
        		"context":bill,
        		 "student":contexts
        }
        html = template.render(context)
        pdf = render_to_pdf('pdf/invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

class TeacherSubjectView(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,CreateView):
	model=Teacher_Subject
	# form_class=Teacher_Attendence_Form
	template_name='teacher/subject.html'
	
	success_message = "new subject was added to present list"
	fields=['user_name','subject','class_name']
	def form_valid(self,form):
		# form.instance.user=self.request.user
		# form.instance.user_id=self.request.user.id
		print(form.cleaned_data)
		return super().form_valid(form)
	def test_func(self):
		# teacher=self.get_object()
		if self.request.user.username=='admin':
			return True
		else:
			return False
	