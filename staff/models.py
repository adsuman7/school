from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.contrib.messages.views import SuccessMessageMixin

# Create your models here.
class Staffinfo(models.Model):
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	subjects=models.CharField(max_length=100,default="idk")
	email_address=models.EmailField(max_length=100)
	salary=models.IntegerField()
	date_of_birth=models.DateField()
	date_join=models.DateField()
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	living_address=models.CharField(max_length=100)
	introduction=models.TextField(blank=True,null=True)
	subject=models.CharField(max_length=100,default=None)
	salarypay_date=models.DateField(blank=True,null=True)
	due=models.IntegerField(default=0,blank=True,null=True)
	type_of_staff=models.CharField(max_length=100)
	def __str__(self):
		return self.first_name
	def get_absolute_url(self):
# 		# messages.add_message(self.request, messages.INFO, 'form submission success')
		return reverse('staff-create')
class Attendence(models.Model):
	perfomance=models.TextChoices('perfomance','A P')
	attendence=models.CharField(choices=perfomance.choices,max_length=10)
	staffinfo=models.ForeignKey(Staffinfo,on_delete=models.CASCADE)
	date=models.DateField(default=timezone.now)
	def get_absolute_url(self):
		# messages.add_message(self.request, messages.INFO, 'form submission success')
		return reverse('staff-attendence')
class Staff_Payment_Bill(models.Model):
	staffinfo=models.ForeignKey(Staffinfo,on_delete=models.CASCADE)
	bill_payer_name=models.CharField(max_length=100)
	paid_amount=models.IntegerField()
	due_amount=models.IntegerField()
	paid_date=models.DateField(default=timezone.now)
	# def get_absolute_url(self):
	# 	# messages.add_message(self.request, messages.INFO, 'form submission success')
	# 	return reverse('salary-pdf',kwargs={"pk":self.})




