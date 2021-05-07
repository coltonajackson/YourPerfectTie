from django.urls import path
from .views import (
	SignUpView, EditProfileView, CustomUserUpdateView, CustomUserDetailView,
	CustomUserDeleteView, CustomUserListView, CustomUserCreateView
)

urlpatterns = [
	# Current User URLs
	path('signup/', SignUpView.as_view(), name='signup'),
	path(r'^(?P<pk>\d+)/$', EditProfileView.as_view(), name='edit_profile'),
	# Any Known User URLs
	path('<int:pk>/edit/', CustomUserUpdateView.as_view(), name='user_edit'),
	path('<int:pk>/delete/', CustomUserDeleteView.as_view(), name='user_delete'),
	path('<int:pk>/', CustomUserDetailView.as_view(), name='user_detail'),
	path('new/', CustomUserCreateView.as_view(), name='user_new'),
	path('', CustomUserListView.as_view(), name='user_list'),
]