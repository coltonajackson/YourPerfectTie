from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import (
	ItemListView, ItemDetailView, ItemUpdateView, ItemDeleteView, ItemCreateView, 
	CommentDetailView, CommentCreateView, CommentUpdateView, CommentDeleteView,
)

urlpatterns = [
	path('', ItemListView.as_view(), name='item_list'),
	path('new/', ItemCreateView.as_view(), name='item_new'),
	path('<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
	path('<int:pk>/edit/', ItemUpdateView.as_view(), name='item_edit'),
	path('<int:pk>/delete/', ItemDeleteView.as_view(), name='item_delete'),
	path('comment/<int:pk>/', CommentDetailView.as_view(), name='comment_detail'),
	path('comment/new/', CommentCreateView.as_view(), name='comment_create'),
	path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_create'),
	path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]