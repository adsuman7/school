from django.urls import path
from .views import (
		StaffCreateView,
		StaffListView,
		StaffDetailView,
		StaffUpdateView,
		StaffAttendenceView,
		StaffSalaryView,
		GeneratePDF,
	)

urlpatterns = [
    path('staff/new/',StaffCreateView.as_view(),name="staff-create"),
    path('staff/list/',StaffListView.as_view(),name="staff-list"),
    path('staff/detail/<int:pk>/',StaffDetailView.as_view(),name="staff-detail"),
    path('staff/update/<int:pk>/',StaffUpdateView.as_view(),name="staff-update"),
    path('staff/salary/<int:pk>/',StaffSalaryView.as_view(),name="staff-salary"),
    path('staff/attendence/',StaffAttendenceView.as_view(),name="staff-attendence"),
    # path('staff/subject/add',StaffSubjectView.as_view(),name="staff-add"),
    path('staff/pdf/<int:pk>/',GeneratePDF.as_view(),name="staff-pdf"),
    # path('',IndexView.as_view(),name="index"),

]
