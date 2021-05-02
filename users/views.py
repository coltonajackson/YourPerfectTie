from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class SignUpView(CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'users/signup.html'

class EditProfileView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = CustomUser
	#form_class = CustomUserChangeForm
	fields = ('username', 'first_name', 'last_name', 'email', 'age',)
	template_name = 'edit_profile.html'
	success_url = reverse_lazy('home')
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj == self.request.user

class CustomUserListView(ListView):
	model = CustomUser
	template_name = 'users/user_list.html'

class CustomUserDetailView(DetailView):
	model = CustomUser
	template_name = 'users/user_detail.html'

class CustomUserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
	model = CustomUser
	permission_required = ('users.edit',)
	if (get_user_model().is_superuser):
		fields = ('username', 'first_name', 'last_name', 'email', 'age', 'is_staff', 'is_superuser', 'is_active')
	else:
		fields = ('username', 'first_name', 'last_name', 'email', 'age')
	template_name = 'users/user_edit.html'
	success_url = reverse_lazy('user_list')
	login_url = 'login'

class CustomUserDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
	model = CustomUser
	permission_required = ('users.delete',)
	template_name = 'users/user_delete.html'
	success_url = reverse_lazy('user_list')
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj.is_superuser

class CustomUserCreateView(LoginRequiredMixin, CreateView):
	model = CustomUser
	if (get_user_model().is_superuser):
		fields = ('username', 'first_name', 'last_name', 'email', 'age', 'is_staff', 'is_superuser', 'is_active')
	else:
		fields = ('username', 'first_name', 'last_name', 'email', 'age')
	template_name = 'users/user_new.html'
	success_url = reverse_lazy('user_list')
	login_url = 'login'

	def form_valid(self, form):
		form.instance.publisher = self.request.user
		return super().form_valid(form)