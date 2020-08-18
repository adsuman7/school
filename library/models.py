from django.db import models
from teacher.models import Teacherinfo,Teacher_Subject
from student.models import Studentinfo
# Create your models here.
from datetime import date
from django.utils import timezone
from django.urls import reverse

class Book(models.Model):
	name=models.CharField(max_length=100)
	total_quantity=models.IntegerField()
	edition=models.CharField(max_length=100)
	writer=models.CharField(max_length=100)
	subject=models.ForeignKey(Teacher_Subject,on_delete=models.CASCADE,blank=True,null=True)
	remaining_quantity=models.IntegerField()
	def get_absolute_url(self):
		return reverse('bookspec-create')
	def __str__(self):
		return self.name
class Book_Specification(models.Model):
	book=models.ForeignKey(Book,on_delete=models.CASCADE)
	book_number=models.IntegerField()
	teacherinfo=models.ForeignKey(Teacherinfo,on_delete=models.CASCADE,blank=True,null=True)
	studentinfo=models.ForeignKey(Studentinfo,on_delete=models.CASCADE,blank=True,null=True)
	date_issue=models.DateField(default=timezone.now)
	date_return=models.DateField(blank=True,null=True)
	def get_absolute_url(self):
		return reverse('book-create')
	def __str__(self):
		return self.book.name
class booked(models.Model):
	book_specification=models.ForeignKey(Book_Specification,on_delete=models.CASCADE)
	teacherinfo=models.ForeignKey(Teacherinfo,on_delete=models.CASCADE,blank=True,null=True)
	studentinfo=models.ForeignKey(Studentinfo,on_delete=models.CASCADE,blank=True,null=True)
	date_issue=models.DateField(blank=True,null=True)
	date_return=models.DateField(blank=True,null=True)
	# def __str__(self):
	# 	return self.book_specification
