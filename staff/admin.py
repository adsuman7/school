from django.contrib import admin


# Register your models here.
from .models import Staffinfo
# from .models import Teacher_Subject
admin.site.register(Staffinfo)
# admin.site.register(Teacher_Subject)