from django.urls import path
from .views import SignUpView, EditProfileView

urlpatterns = [
	path('signup/', SignUpView.as_view(), name='signup'),
	#path('<int:pk>/', EditProfileView.as_view(), name='edit_profile'),
	path('edit_profile/', EditProfileView.as_view(), name='edit_profile'),
]