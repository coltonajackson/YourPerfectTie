from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Category

class CategoryListView(ListView):
	model = Category
	template_name = 'categories/category_list.html'

class CategoryDetailView(DetailView):
	model = Category
	template_name = 'categories/category_detail.html'

class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
	model = Category
	permission_required = ('categories.edit',)
	fields = ('name', 'gender')
	template_name = 'categories/category_edit.html'
	login_url = 'login'

class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
	model = Category
	permission_required = ('categories.delete',)
	template_name = 'categories/category_delete.html'
	success_url = reverse_lazy('category_list')
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj.publisher == self.request.user

class CategoryCreateView(LoginRequiredMixin, CreateView):
	model = Category
	fields = ('name', 'gender')
	template_name = 'categories/category_new.html'
	login_url = 'login'

	def form_valid(self, form):
		form.instance.publisher = self.request.user
		return super().form_valid(form)