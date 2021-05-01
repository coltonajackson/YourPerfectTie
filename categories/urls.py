from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import (
	CategoryListView, CategoryDetailView, CategoryUpdateView, CategoryDeleteView, CategoryCreateView,
)

urlpatterns = [
    path('<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_edit'),
	path('<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
	path('new/', CategoryCreateView.as_view(), name='category_new'),
	path('', CategoryListView.as_view(), name='category_list'),
]