from django.urls import path
from . import views
from .views import (
		BookCreateView,
		Book_SpecificationCreateView,
		BookListView,
		# BlogDetailView,
		# BlogUpdateView
	)

urlpatterns = [
    path('library/book/new/',BookCreateView.as_view(),name="book-create"),
    path('library/book/booked/',Book_SpecificationCreateView.as_view(),name="bookspec-create"),
    path('library/book/list/',BookListView.as_view(),name="book-list"),
    path('library/book/booked/<int:pk>/',views.bookdetailview,name="book-booked"),




   ]