from django.contrib import admin

# Register your models here.
from .models import Teacherinfo
from .models import Teacher_Subject
admin.site.register(Teacherinfo)
admin.site.register(Teacher_Subject)