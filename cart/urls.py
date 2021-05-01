from django.urls import path, include

from .views import (
    ListCartView, DetailCartView, CreateCartView, UpdateCartView, DeleteCartView,
    ListCartItemView, DetailCartItemView, CreateCartItemView, UpdateCartItemView, DeleteCartItemView,
)

# Cart Urls
urlpatterns = [
    path('cart/', ListCartView.as_view(), name='list-carts'),
    path('cart/<int:pk>/', DetailCartView.as_view(), name='detail-cart'),
    path('cart/create/', CreateCartView.as_view(), name='create-cart'),
    path('cart/<int:pk>/update/', UpdateCartView.as_view(), name='update-cart'),
    path('cart/<int:pk>/delete/', DeleteCartView.as_view(), name='delete-cart'),
]

# CartItem Urls
urlpatterns += [
    path('cartitem/', ListCartItemView.as_view(), name='list-cartitem'),
    path('cartitem/<int:pk>/', DetailCartItemView.as_view(), name='detail-cartitem'),
    path('cartitem/create/', CreateCartItemView.as_view(), name='create-cartitem'),
    path('cartitem/<int:pk>/update/', UpdateCartItemView.as_view(), name='update-cartitem'),
    path('cartitem/<int:pk>/delete/', DeleteCartItemView.as_view(), name='delete-cartitem'),
]