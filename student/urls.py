from django.urls import path
from . import views
from .views import (
		StudentDetailView,
		StudentCreateView,
		StudentFee,
		GeneratePDF,
		AttendenceView
			)

urlpatterns = [
    
    path('student/profile/<int:pk>/',StudentDetailView.as_view(),name="student-profile"),
    path('student/profile/',StudentCreateView.as_view(),name="student-create"),
    path('student/fee/<int:pk>/',StudentFee.as_view(),name="student-fee"),

    path('student/invoice/<int:pk>/',GeneratePDF.as_view(),name="invoice-pdf"),
    # path('student/attendence/<int:grade>/',views.Attendence_View,name="attendence-create"),
   path('student/attendence/<int:grade>/',AttendenceView.as_view(),name="attendence-create"),
   path('student/assignment/<int:grade>/',views.Assignment_View,name="assignment-create"),
    path('student/assessment/<int:grade>/',views.Assessment_View,name="assessment-create"), 

]
