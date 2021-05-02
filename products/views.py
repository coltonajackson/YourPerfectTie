from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Product, Comment

class ProductListView(ListView):
	model = Product
	template_name = 'products/product_list.html'

class ProductDetailView(DetailView):
	model = Product
	template_name = 'products/product_detail.html'

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Product
	fields = ('name', 'description', 'category', 'current_price', 'main_image')
	template_name = 'products/product_edit.html'
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj.publisher == self.request.user

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Product
	template_name = 'products/product_delete.html'
	success_url = reverse_lazy('product_list')
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj.publisher == self.request.user

class ProductCreateView(LoginRequiredMixin, CreateView):
	model = Product
	fields = ('name', 'description', 'category', 'current_price', 'main_image')
	template_name = 'products/product_new.html'
	login_url = 'login'

	def form_valid(self, form):
		form.instance.publisher = self.request.user
		return super().form_valid(form)

class CommentDetailView(LoginRequiredMixin, DetailView):
	model = Comment
	template_name = 'comments/comment_detail.html'
	login_url = 'login'

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Comment
	fields = ('comment',)
	template_name = 'comments/comment_edit.html'
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj.publisher == self.request.user

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Comment
	template_name = 'comments/comment_delete.html'
	success_url = reverse_lazy('product_detail')
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj.publisher == self.request.user

class CommentCreateView(LoginRequiredMixin, CreateView):
	model = Comment
	fields = ('comment',)
	template_name = 'comments/comment_new.html'
	login_url = 'login'

	def form_valid(self, form):
		form.instance.publisher = self.request.user
		return super().form_valid(form)
