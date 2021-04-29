from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import CustomUserCreationForm, CustomUserChangeForm

class SignUpView(CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'

class EditProfileView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	form_class = CustomUserChangeForm
	success_url = reverse_lazy('home')
	template_name = 'edit_profile.html'
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj.customuser == self.request.user