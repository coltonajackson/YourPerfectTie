from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import (
	ProductListView, ProductDetailView, ProductUpdateView, ProductDeleteView, ProductCreateView, 
	CommentDetailView, CommentCreateView, CommentUpdateView, CommentDeleteView,
)

urlpatterns = [
	path('', ProductListView.as_view(), name='product_list'),
	path('new/', ProductCreateView.as_view(), name='product_new'),
	path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
	path('<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
	path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
	path('<int:fk>/comment/<int:pk>/', CommentDetailView.as_view(), name='comment_detail'),
	path('<int:fk>/comment/new/', CommentCreateView.as_view(), name='comment_new'),
	path('<int:fk>/comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_edit'),
	path('<int:fk>/comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]