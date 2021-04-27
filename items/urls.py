from django.urls import path
from .views import (
	ItemListView, ItemDetailView, ItemUpdateView, ItemDeleteView, ItemCreateView, 
	CommentDetailView, CommentCreateView, CommentUpdateView, CommentDeleteView,
)

urlpatterns = [
	path('<int:fk>/comment/<int:pk>/', CommentDetailView.as_view(), name='comment_detail'),
	path('<int:fk>/comment/new/', CommentCreateView.as_view(), name='comment_create'),
	path('<int:fk>/comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_create'),
	path('<int:fk>/comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
	path('<int:pk>/edit/', ItemUpdateView.as_view(), name='item_edit'),
	path('<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
	path('<int:pk>/delete/', ItemDeleteView.as_view(), name='item_delete'),
	path('new/', ItemCreateView.as_view(), name='item_new'),
	path('', ItemListView.as_view(), name='item_list'),
]