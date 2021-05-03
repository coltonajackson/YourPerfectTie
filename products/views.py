from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
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

class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
	model = Product
	permission_required = ('product.edit',)
	fields = ('name', 'description', 'category', 'current_price', 'main_image')
	template_name = 'products/product_edit.html'
	login_url = 'login'

class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
	model = Product
	permission_required = ('product.delete')
	template_name = 'products/product_delete.html'
	success_url = reverse_lazy('product_list')
	login_url = 'login'

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

class CommentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
	model = Comment
	permission_required = ('comment.edit',)
	fields = ('comment',)
	template_name = 'comments/comment_edit.html'
	login_url = 'login'

class CommentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
	model = Comment
	permission_required = ('comment.delete',)
	template_name = 'comments/comment_delete.html'
	success_url = reverse_lazy('product_detail')
	login_url = 'login'

class CommentCreateView(LoginRequiredMixin, CreateView):
	model = Comment
	fields = ('comment',)
	template_name = 'comments/comment_new.html'
	login_url = 'login'

	def form_valid(self, form):
		form.instance.publisher = self.request.user
		return super().form_valid(form)
