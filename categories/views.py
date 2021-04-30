from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Category

class CategoryListView(ListView):
	model = Category
	template_name = 'category_list.html'

class CategoryDetailView(DetailView):
	model = Category
	template_name = 'category_detail.html'

class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Category
	fields = ('name', 'gender')
	template_name = 'category_edit.html'
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj.publisher == self.request.user

class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Category
	template_name = 'category_delete.html'
	success_url = reverse_lazy('category_list')
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj.publisher == self.request.user

class CategoryCreateView(LoginRequiredMixin, CreateView):
	model = Category
	fields = ('name', 'gender')
	template_name = 'category_new.html'
	login_url = 'login'

	def form_valid(self, form):
		form.instance.publisher = self.request.user
		return super().form_valid(form)