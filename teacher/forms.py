from django import forms
from .models import Teacherinfo

class TeacherInfoForm(forms.ModelForm):


	class Meta:
		model=Teacherinfo
		fields=['first_name','last_name','email_address','salary','living_address','date_of_birth','date_join','introduction','subject']


class TeacherUpdateForm(forms.ModelForm):

	class Meta:
		model=Teacherinfo
		fields=['first_name','last_name','email_address','living_address','date_of_birth','introduction','subject']	

class Feepayment(forms.Form):
	given=forms.IntegerField()
	bill_payer_name=forms.CharField(max_length=100)	
