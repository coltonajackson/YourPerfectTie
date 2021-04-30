from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Item, Comment

class ItemListView(ListView):
	model = Item
	template_name = 'item_list.html'

class ItemDetailView(DetailView):
	model = Item
	template_name = 'item_detail.html'

class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Item
	fields = ('name', 'description', 'current_price')
	template_name = 'item_edit.html'
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj.publisher == self.request.user

class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Item
	template_name = 'item_delete.html'
	success_url = reverse_lazy('item_list')
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj.publisher == self.request.user

class ItemCreateView(LoginRequiredMixin, CreateView):
	model = Item
	fields = ('name', 'description', 'category', 'current_price', 'main_image')
	template_name = 'item_new.html'
	login_url = 'login'

	def form_valid(self, form):
		form.instance.publisher = self.request.user
		return super().form_valid(form)

class CommentDetailView(LoginRequiredMixin, DetailView):
	model = Comment
	template_name = 'comment_detail.html'
	login_url = 'login'

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Comment
	fields = ('comment',)
	template_name = 'comment_edit.html'
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj.publisher == self.request.user

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Comment
	template_name = 'comment_delete.html'
	success_url = reverse_lazy('item_detail')
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj.publisher == self.request.user

class CommentCreateView(LoginRequiredMixin, CreateView):
	model = Item
	fields = ('comment',)
	template_name = 'comment_new.html'
	login_url = 'login'

	def form_valid(self, form):
		form.instance.publisher = self.request.user
		return super().form_valid(form)
