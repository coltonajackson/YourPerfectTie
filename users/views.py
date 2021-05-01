from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class SignUpView(CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'

class EditProfileView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = CustomUser
	form_class = CustomUserChangeForm
	success_url = reverse_lazy('home')
	template_name = 'edit_profile.html'
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj == self.request.user

class CustomUserListView(ListView):
	model = CustomUser
	template_name = 'user_list.html'

class CustomUserDetailView(DetailView):
	model = CustomUser
	template_name = 'user_detail.html'

class CustomUserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = CustomUser
	if (get_user_model().is_superuser):
		fields = ('username', 'first_name', 'last_name', 'email', 'age', 'is_staff', 'is_superuser', 'is_active')
	else:
		fields = ('username', 'first_name', 'last_name', 'email', 'age')
	template_name = 'user_edit.html'
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj == self.request.user

class CustomUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = CustomUser
	template_name = 'user_delete.html'
	success_url = reverse_lazy('user_list')
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj == self.request.user

class CustomUserCreateView(LoginRequiredMixin, CreateView):
	model = CustomUser
	fields = ('username', 'first_name', 'last_name', 'email', 'age')
	template_name = 'user_new.html'
	login_url = 'login'

	def form_valid(self, form):
		form.instance.publisher = self.request.user
		return super().form_valid(form)