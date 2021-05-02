from django.urls import path
from django.contrib.auth import views as auth_views
from shop import views
from .views import add_to_cart, remove_from_cart, get_cart, CartPageView

urlpatterns = [
	path('', views.index, name='home'),
	#path('', HomePageView.as_view(), name='home'),
	path('cart/', CartPageView.as_view(), name='cart'),
	path('add_to_cart/<int:item_id>/', add_to_cart, name='add_to_cart'),
	path('remove_from_cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
	#path('cart/', get_cart(), name='cart'),
	path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]