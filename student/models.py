from django.db import models
from teacher.models import Teacherinfo
from phone_field import PhoneField
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from django.utils import timezone


# Create your models here.
class Studentinfo(models.Model):
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	date_of_birth=models.DateField()
	date_join=models.DateField()
	Father_name=models.CharField(max_length=100)
	mother_name=models.CharField(max_length=100)
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	living_address=models.CharField(max_length=100)
	class_name=models.IntegerField()
	fees=models.IntegerField()
	contact=PhoneField(blank=True, help_text='Contact phone number')
	feepay_date=models.DateField(blank=True,null=True)
	due=models.IntegerField(default=0,blank=True,null=True)
	def get_absolute_url(self):
		return reverse('/')
	def __str__(self):
		return self.first_name

class Student_Evaluation(models.Model):
	perfomance=models.TextChoices('perfomance','A B C D E')
	creativity=models.CharField(blank=True,choices=perfomance.choices,max_length=10)
	Attendence=models.CharField(blank=True,choices=perfomance.choices,max_length=10)
	Assignment=models.CharField(blank=True,choices=perfomance.choices,max_length=10)
	discipline=models.CharField(blank=True,choices=perfomance.choices,max_length=10)
	#extra_curricular=models.CharField(blank=True,choices=perfomance.choices,max_length=10)
	studentinfo=models.OneToOneField(Studentinfo,on_delete=models.CASCADE)


class Assignment(models.Model):
	title=models.CharField(max_length=100)
	topic=models.TextField()
	perfomance=models.TextChoices('perfomance','A B C D E')
	grade=models.CharField(blank=True,choices=perfomance.choices,max_length=10)
	subject=models.CharField(max_length=100)
	studentinfo=models.ForeignKey(Studentinfo,on_delete=models.CASCADE)
	teacherinfo=models.ForeignKey(Teacherinfo,on_delete=models.CASCADE)

class Assessment(models.Model):
	title=models.CharField(max_length=100)
	perfomance=models.TextChoices('perfomance','A B C D E')
	grade=models.CharField(blank=True,choices=perfomance.choices,max_length=10)
	subject=models.CharField(max_length=100)
	studentinfo=models.ForeignKey(Studentinfo,on_delete=models.CASCADE)
	teacherinfo=models.ForeignKey(Teacherinfo,on_delete=models.CASCADE)
	marks_obtained=models.IntegerField()
	full_marks=models.CharField(max_length=100)
	pass_marks=models.CharField(max_length=100)

class Student_Payment_Bill(models.Model):
	studentinfo=models.ForeignKey(Studentinfo,on_delete=models.CASCADE)
	bill_payer_name=models.CharField(max_length=100)
	paid_amount=models.IntegerField()
	due_amount=models.IntegerField()
	paid_date=models.DateField(default=timezone.now)
class Attendence(models.Model):
	perfomance=models.TextChoices('perfomance','A P')
	attendence=models.CharField(choices=perfomance.choices,max_length=10)
	studentinfo=models.ForeignKey(Studentinfo,on_delete=models.CASCADE)
	date=models.DateField(default=timezone.now)
	def get_absolute_url(self):
		return reverse('/')