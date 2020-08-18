from django.urls import path
from .views import (
		BlogCreateView,
		BlogListView,
		BlogDetailView,
		BlogUpdateView,
		NoticeCreateView,
		NoticeListView,
		NoticeDetailView,
		NoticeUpdateView
	)

urlpatterns = [
    path('blog/new/',BlogCreateView.as_view(),name="blog-create"),
    path('blog/list/',BlogListView.as_view(),name="blog-list"),
    path('blog/detail/<int:pk>/',BlogDetailView.as_view(),name="blog-detail"),
    path('blog/update/<int:pk>/',BlogUpdateView.as_view(),name="blog-update"),
    path('notice/new/',NoticeCreateView.as_view(),name="notice-create"),
    path('notice/list/',NoticeListView.as_view(),name="notice-list"),
    path('notice/detail/<int:pk>/',NoticeDetailView.as_view(),name="notice-detail"),
    path('notice/update/<int:pk>/',NoticeUpdateView.as_view(),name="notice-update"),
]
