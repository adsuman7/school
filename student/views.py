from django.shortcuts import render
from .models import Studentinfo,Student_Payment_Bill,Attendence,Assignment,Teacherinfo
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
#from django.views import View
from datetime import date 
from .forms import feepayment,Attendence_Form,Assignment_Form,Assessment_Form
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.core.mail import send_mail


from school.utils import render_to_pdf
# Create your views here.
from django.views.generic import (
		ListView,
		DetailView,
		CreateView,
		UpdateView,
		DeleteView

	)
# Create your views here.
class StudentDetailView(LoginRequiredMixin,UserPassesTestMixin,DetailView):
	model=Studentinfo
	template_name='student/student_profile_view.html'
	context_object_name='student'
	def form_valid(self,form):
		form.instance.user=self.request.user
		print(form.cleaned_data)
		return super().form_valid(form)
	def test_func(self):
		student=self.get_object()
		if self.request.user==student.user:
			return True
		else:
			return False
class StudentCreateView(LoginRequiredMixin,CreateView):
	model=Studentinfo
	template_name='student/student_create_view.html'
	fields=['first_name','last_name','date_of_birth','date_join','Father_name','mother_name','living_address','class_name','fees','contact']
	def form_valid(self,form):
		form.instance.user=self.request.user
		print(form.cleaned_data)
		return super().form_valid(form)

class StudentFee(LoginRequiredMixin,View):
	def get(self,request,pk,*args,**kwargs):
		context=Studentinfo.objects.get(id=pk)
		date_join=context.date_join
		due=int(context.due)
			#context=int(context.fees) + 200
		today = date.today()
		t=today-context.feepay_date
		month=int(abs(t.days)/30)
		fees=month*int(context.fees)+due

		form=feepayment()
		pay_date=context.feepay_date
		context={"form":form,"fees":fees,"pay_date":pay_date}
		return render(request,'student/student_fee.html',context)
	
	def post(self,request,pk,*args,**kwargs):
		context=Studentinfo.objects.get(id=pk)
		date_join=context.date_join
		due=int(context.due)
			#context=int(context.fees) + 200
		today = date.today()
		t=today-context.feepay_date
		month=int(abs(t.days)/30)
		fees=month*int(context.fees)+due		
		form=feepayment(request.POST)
		if form.is_valid():
			given=int(form.cleaned_data['given'])
			name=form.cleaned_data['bill_payer_name']
			due=fees-given
			context.due=due
			context.feepay_date=today
			context.save(update_fields=['feepay_date','due'])
			bill=Student_Payment_Bill(studentinfo=context,bill_payer_name=name,paid_amount=given,due_amount=due)
			bill.save()
			return HttpResponse("ALMOST THERE")
def studentgetfee(request,pk):
	if request.method=="POST":
		form=feepayment(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/success/')
	else:
		form=feepayment()
	return render(request,'student/student_fee.html',{'form':form})


class GeneratePDF(View):
    def get(self,request,pk,*args, **kwargs):
        template = get_template('pdf/invoice.html')
        contexts=Studentinfo.objects.get(id=pk)
        bill=Student_Payment_Bill.objects.filter(studentinfo=contexts).order_by('-id')[0]
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
 
def Attendence_View(request,grade):
	grade=Studentinfo.objects.filter(class_name=grade)
	# classnames={'class_names':classnames}
	# grade={'grade':grade}
	# grade=get_object_or_404(Studentinfo, class_name=grade)
	# print(grade['grade'])
	if request.method=="POST":
		form=Attendence_Form(grade,request.POST)
		print(form)
		if form.is_valid():
			print(form)
			form.save()
			return HttpResponse('/success/')
	else:
		form=Attendence_Form(grade)

	return render(request,"student/attendence.html",{'form':form,'grade':grade})

class AttendenceView(View):
	
	def get(self,request,grade):
		grade=Studentinfo.objects.filter(class_name=grade)
		# studentinfo=Studentinfo.objects.get(class_name=grade)
		#print(studentinfo)
		# grade={'grade':grade}
		form=Attendence_Form(grade)
		return render(request,"student/attendence.html",{'form':form,'grade':grade})

	def post(self,request,grade):
		grade=Studentinfo.objects.filter(class_name=grade)
		
		
		form=Attendence_Form(grade,request.POST)
		# a=form.cleaned_data['studentinfo']
		# print(a)
		if form.is_valid():
			if(form.cleaned_data['attendence']=='A'):
				a=form.cleaned_data['studentinfo']

				subject = 'Attendence'
				message = f' your children {a} is absent '
				email_from = settings.EMAIL_HOST_USER
				recipient_list = ['adsuman7@gmail.com',]
				send_mail( subject, message, email_from, recipient_list,fail_silently=False,)
			form.save()
			return HttpResponse('success')
# class AttendenceView(CreateView):
# 	model=Attendence
# 	form_class=Attendence_Form

# 	def form_valid(self,form):
# 		# form.instance.class_name=self.kwargs['grade']
# 		return super().form_valid(form)
# 	def get_form_kwargs(self):
# 		kwargs = super(AttendenceView, self).get_form_kwargs()
		
# 		kwargs['grade'] = self.kwargs['grade']
# 		# kwargs.update({'grade': self.grade})
# 		return kwargs

# # def get_form_kwargs(self):
# #  #        kwargs = super(PlaceEventFormView, self).get_form_kwargs()
# #  #        kwargs.update({'grade': self.grade})
# #  #        return kwargs
def Assignment_View(request,grade):
	grades=Studentinfo.objects.filter(class_name=grade)
	# classnames={'class_names':classnames}
	# grade={'grade':grade}
	# grade=get_object_or_404(Studentinfo, class_name=grade)
	# print(grade['grade'])
	if request.method=="POST":
		form=Assignment_Form(grades,request.POST)
		print(form)
		if form.is_valid():
			form.instance.teacherinfo=Teacherinfo.objects.get(user=request.user)
			print(form)
			form.save()
			return HttpResponse('/success/')
	else:
		form=Assignment_Form(grades)

	return render(request,"student/attendence.html",{'form':form,'grade':grades})			

def Assessment_View(request,grade):
	grades=Studentinfo.objects.filter(class_name=grade)
	# classnames={'class_names':classnames}
	# grade={'grade':grade}
	# grade=get_object_or_404(Studentinfo, class_name=grade)
	# print(grade['grade'])
	if request.method=="POST":
		form=Assessment_Form(grades,request.POST)
		print(form)
		if form.is_valid():
			form.instance.teacherinfo=Teacherinfo.objects.get(user=request.user)
			print(form)
			form.save()
			return HttpResponse('/success/')
	else:
		form=Assessment_Form(grades)

	return render(request,"student/attendence.html",{'form':form,'grade':grades})			













