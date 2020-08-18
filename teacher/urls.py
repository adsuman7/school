from django.urls import path
from .views import (
		TeacherCreateView,
		TeacherListView,
		TeacherDetailView,
		TeacherUpdateView,
		TeacherAttendenceView,
		TeacherSalaryView,
		GeneratePDF,
		IndexView,
		TeacherSubjectView

	)

urlpatterns = [
    path('teacher/new/',TeacherCreateView.as_view(),name="teacher-create"),
    path('teacher/list/',TeacherListView.as_view(),name="teacher-list"),
    path('teacher/detail/<int:pk>/',TeacherDetailView.as_view(),name="teacher-detail"),
    path('teacher/update/<int:pk>/',TeacherUpdateView.as_view(),name="teacher-update"),
    path('teacher/salary/<int:pk>/',TeacherSalaryView.as_view(),name="teacher-salary"),
    path('teacher/attendence/',TeacherAttendenceView.as_view(),name="teacher-attendence"),
    path('teacher/subject/add',TeacherSubjectView.as_view(),name="subject-add"),
    path('salary/pdf/<int:pk>/',GeneratePDF.as_view(),name="salary-pdf"),
    path('',IndexView.as_view(),name="index"),

]
