from .models import booked
from django import forms

class Books(forms.ModelForm):
	class Meta:
		model=booked
		fields=['book_specification','teacherinfo','studentinfo','date_issue','date_return']