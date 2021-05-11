from django.urls import path
from django.contrib.auth import views as auth_views
# from .views import HomePageView, CreateCheckoutSessionView
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('featured_items', views.featured_items, name='featured_items'),
	path('category_items/<int:pk>', views.category_items, name='category_items'),
	# path('', HomePageView.as_view(), name='home'),
	# path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name="create-checkout-session"),
	path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]