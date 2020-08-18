from django import forms
from .models import Staffinfo
class DateInput(forms.DateInput):
	input_type='date'
class StaffInfoForm(forms.ModelForm):
	class Meta:
		model=Staffinfo
		fields=['user','first_name','last_name','email_address','salary','living_address','date_of_birth','date_join','introduction','subject','salarypay_date','due','type_of_staff']
		widgets={'date_of_birth':DateInput(),'date_join':DateInput(),'date_of_birth':DateInput(),'salarypay_date':DateInput()}

class Feepayment(forms.Form):
	given=forms.IntegerField()
	bill_payer_name=forms.CharField(max_length=100)	
