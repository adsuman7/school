from django import forms
from .models import Attendence
from .models import Studentinfo,Assignment,Teacherinfo,Assessment
class feepayment(forms.Form):
	given=forms.IntegerField()
	bill_payer_name=forms.CharField(max_length=100)

class Attendence_Form(forms.ModelForm):
	#studentinfo=forms.ModelChoiceField(queryset=Studentinfo.objects.get(class_name=grade))
	class Meta:
		model=Attendence
		fields=['studentinfo','attendence']
	def __init__(self ,grade,*args, **kwargs):
		
		# kwargs = super(Attendence_Form, self).get_form_kwargs()
		super(Attendence_Form, self).__init__(*args, **kwargs)
		# print(kwargs.pop("grade"))
		# grade = int((kwargs.pop("grade")))
		# print(classnames)
		# grades=grade['grade']
		# grade=kwargs.pop('grade')
		# print(grades)
		# a = Studentinfo.objects.filter(class_name=grade['grade'])
		#print(a)
		# self.fields['studentinfo']=forms.ModelChoiceField(queryset=Studentinfo.objects.filter(class_name=grade.class_name))
		# self.fields['studentinfo'] = ([(s.pk,s) for s in grade])
		
		self.fields['studentinfo'].queryset=grade

class Assignment_Form(forms.ModelForm):
	#studentinfo=forms.ModelChoiceField(queryset=Studentinfo.objects.get(class_name=grade))
	class Meta:
		model=Assignment
		fields=['studentinfo','title','subject','grade']
	def __init__(self ,grades,*args, **kwargs):
		
		super(Assignment_Form, self).__init__(*args, **kwargs)
		# print(kwargs.pop("grade"))
		# grade = int((kwargs.pop("grade")))
		# print(classnames)
		# grades=grade['grade']
		# grade=kwargs.pop(grade)
		# print(grades)
		# a = Studentinfo.objects.filter(class_name=grades)
		#print(a)
		# self.fields['studentinfo']=forms.ModelChoiceField(queryset=Studentinfo.objects.filter(class_name=grade.class_name))
		# self.fields['studentinfo'] = ([(s.pk,s) for s in grade])
		
		self.fields['studentinfo'].queryset=grades

class Assessment_Form(forms.ModelForm):
	#studentinfo=forms.ModelChoiceField(queryset=Studentinfo.objects.get(class_name=grade))
	class Meta:
		model=Assessment
		fields=['studentinfo','title','subject','grade','marks_obtained']
	def __init__(self ,grades,*args, **kwargs):
		
		super(Assessment_Form, self).__init__(*args, **kwargs)
		# print(kwargs.pop("grade"))
		# grade = int((kwargs.pop("grade")))
		# print(classnames)
		# grades=grade['grade']
		# grade=kwargs.pop(grade)
		# print(grades)
		# a = Studentinfo.objects.filter(class_name=grades)
		#print(a)
		# self.fields['studentinfo']=forms.ModelChoiceField(queryset=Studentinfo.objects.filter(class_name=grade.class_name))
		# self.fields['studentinfo'] = ([(s.pk,s) for s in grade])
		
		self.fields['studentinfo'].queryset=grades

# class test(forms.Form):
# 	# studentinfo=forms.ModelChoiceField()
# 	def __init__(self,*args, **kwargs):
# 			classnames = kwargs.get('class_names')
# 			super(Attendence_Form, self).__init__(*args, **kwargs)
# 			#self.fields['studentinfo'] = Studentinfo.objects.get(class_name=grade)
# 			self.fields['studentinfo'].queryset=class_names
