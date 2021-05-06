from django.urls import path
from .views import (
    CartTemplateView, CartDetailView, CartListView, CartCreateView, CartUpdateView, CartDeleteView,
    CartItemDetailView, CartItemListView, CartItemCreateView, CartItemUpdateView, CartItemDeleteView,
)

urlpatterns = [
    # Cart URLs
    path('', CartTemplateView.as_view(), name='cart'),
    #path('', CartListView.as_view(), name='cart_list'),
    path('<int:pk>/', CartDetailView.as_view(), name='cart_detail'),
    path('new/', CartCreateView.as_view(), name='cart_new'),
    path('<int:pk>/edit/', CartUpdateView.as_view(), name='cart_edit'),
    path('<int:pk>/delete/', CartDeleteView.as_view(), name='cart_delete'),
    # CartItem URLs
    path('cartitem/', CartItemListView.as_view(), name='cartitem_list'),
    path('cartitem/<int:pk>/', CartItemDetailView.as_view(), name='cartitem_detail'),
    path('cartitem/new/', CartItemCreateView.as_view(), name='cartitem_new'),
    path('cartitem/<int:pk>/edit/', CartItemUpdateView.as_view(), name='cartitem_edit'),
    path('cartitem/<int:pk>/delete/', CartItemDeleteView.as_view(), name='cartitem_delete'),
]