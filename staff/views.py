from django.shortcuts import render
from .forms import Feepayment,StaffInfoForm
from .models import Staffinfo,Attendence,Staff_Payment_Bill
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
class StaffCreateView(LoginRequiredMixin,CreateView):
	model=Staffinfo
	form_class=StaffInfoForm
	template_name='staff/staff-create.html'
	# fields=['user','first_name','last_name','email_address','salary','living_address','date_of_birth','date_join','introduction','subject','salarypay_date','due','type_of_staff']
	success_url=''
	def form_valid(self,form):
		# form.instance.user=self.request.user
		# form.instance.user_id=self.request.user.id
		print(form.cleaned_data)
		return super().form_valid(form)

class StaffListView(LoginRequiredMixin,ListView):
	model=Staffinfo
	template_name='staff/staff-list.html'
	context_object_name='staffs'

class StaffDetailView(LoginRequiredMixin,UserPassesTestMixin,DetailView):
	model=Staffinfo
	template_name='staff/staff-detail.html'
	context_object_name='staff'
	def form_valid(self,form):
		# form.instance.user=self.request.user
		print(form.cleaned_data)
		return super().form_valid(form)
	def test_func(self):
		# teacher=self.get_object()
		if self.request.user.username=='admin':
			return True
		else:
			return False
class StaffUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model=Staffinfo
	# form_class=StaffUpdateForm
	fields=['user','first_name','last_name','email_address','salary','living_address','date_of_birth','date_join','introduction','type_off_staff']
	template_name='staff/staff-create.html'
	success_url=''
	def form_valid(self,form):
		# form.instance.user=self.request.user
		print(form.cleaned_data)
		return super().form_valid(form)
	def test_func(self):
		# teacher=self.get_object()
		if self.request.user.username=='admin':
			return True
		else:
			return False
class StaffAttendenceView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
	model=Attendence
	# form_class=Teacher_Attendence_Form
	template_name='staff/staff-attendence.html'
	# success_url='teacher-attendence'
	success_message = "%(calculated_field)s was added to present list"
	fields=['staffinfo','attendence']
	def form_valid(self,form):
		# form.instance.user=self.request.user
		# form.instance.user_id=self.request.user.id
		print(form.cleaned_data)
		return super().form_valid(form)
	def get_success_message(self, cleaned_data):

		return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.staffinfo,
        )	
class StaffSalaryView(LoginRequiredMixin,View):
	def get(self,request,pk,*args,**kwargs):
		context=Staffinfo.objects.get(id=pk)

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
		return render(request,'staff/staff-salary.html',context)
	
	def post(self,request,pk,*args,**kwargs):
		context=Staffinfo.objects.get(id=pk)
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
			bill=Staff_Payment_Bill(staffinfo=context,bill_payer_name=name,paid_amount=given,due_amount=due)
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
			return HttpResponseRedirect(reverse('staff-pdf',kwargs={"pk":pk}))
			

class GeneratePDF(View):
    def get(self,request,pk,*args, **kwargs):
        template = get_template('pdf/invoice.html')
        contexts=Staffinfo.objects.get(id=pk)
        bill=Staff_Payment_Bill.objects.filter(staffinfo=contexts).order_by('-id')[0]
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
