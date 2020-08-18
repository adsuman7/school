from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.contrib.messages.views import SuccessMessageMixin
# Create your models here.
class Teacherinfo(models.Model):
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	email_address=models.EmailField(max_length=100)
	salary=models.IntegerField()
	date_of_birth=models.DateField()
	date_join=models.DateField()
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	living_address=models.CharField(max_length=100)
	introduction=models.TextField(blank=True,null=True)
	subject=models.CharField(max_length=100,null=True)
	salarypay_date=models.DateField(blank=True,null=True)
	due=models.IntegerField(default=0,blank=True,null=True)


	def __str__(self):
		return self.first_name
	def get_absolute_url(self):
		return reverse('teacher-detail',kwargs={'pk':self.pk})
class Teacher_Subject(models.Model):
	user_name=models.ForeignKey(Teacherinfo,on_delete=models.CASCADE)
	subject=models.CharField(max_length=50)
	class_name=models.IntegerField(null=True,blank=True)
	avg_score=models.IntegerField(null=True,blank=True)
	def get_absolute_url(self):
		return reverse('subject-add')

class Teacher_Evaluation(models.Model):
	perfomance=models.TextChoices('perfomance','A B C D E')
	creativity=models.CharField(blank=True,choices=perfomance.choices,max_length=10)
	Attendence=models.CharField(blank=True,choices=perfomance.choices,max_length=10)
	Assignment=models.CharField(blank=True,choices=perfomance.choices,max_length=10)
	student_voting=models.CharField(blank=True,choices=perfomance.choices,max_length=10)
	staff_voting=models.CharField(blank=True,choices=perfomance.choices,max_length=10)
class Attendence(models.Model):
	perfomance=models.TextChoices('perfomance','A P')
	attendence=models.CharField(choices=perfomance.choices,max_length=10)
	teacherinfo=models.ForeignKey(Teacherinfo,on_delete=models.CASCADE)
	date=models.DateField(default=timezone.now)
	def get_absolute_url(self):
		# messages.add_message(self.request, messages.INFO, 'form submission success')
		return reverse('teacher-attendence')

class Teacher_Payment_Bill(models.Model):
	teacherinfo=models.ForeignKey(Teacherinfo,on_delete=models.CASCADE)
	bill_payer_name=models.CharField(max_length=100)
	paid_amount=models.IntegerField()
	due_amount=models.IntegerField()
	paid_date=models.DateField(default=timezone.now)
	# def get_absolute_url(self):
	# 	# messages.add_message(self.request, messages.INFO, 'form submission success')
	# 	return reverse('salary-pdf',kwargs={"pk":self.})


