from django.contrib import admin
from .models import Book,Book_Specification,booked

admin.site.register(Book)
admin.site.register(Book_Specification)
admin.site.register(booked)