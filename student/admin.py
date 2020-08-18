from django.contrib import admin
from .models import Studentinfo,Student_Evaluation,Assignment,Assessment,Student_Payment_Bill,Attendence
# Register your models here.
admin.site.register(Studentinfo)
admin.site.register(Student_Evaluation)
admin.site.register(Assignment)
admin.site.register(Assessment)
admin.site.register(Student_Payment_Bill)
admin.site.register(Attendence)