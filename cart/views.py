from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .models import Cart, CartItem

##-------------- Cart Views --------------------------------------
class DetailCartView(DetailView):
    model = Cart
    template_name='cart/detail_cart.html'

class ListCartView(ListView):
    model = Cart
    context_object_name = 'carts'
    template_name='cart/list_cart.html'

class CreateCartView(CreateView):
    model = Cart
    template_name = 'cart/create_cart.html'

class UpdateCartView(UpdateView):
    model = Cart
    template_name = 'cart/edit_cart.html'

class DeleteCartView(DeleteView):
    model = Cart
    template_name = 'cart/delete_cart.html'


##-------------- CartItem Views --------------------------------------
class DetailCartItemView(DetailView):
    model = CartItem
    template_name='cartitem/detail_cartitem.html'

class ListCartItemView(ListView):
    model = CartItem
    context_object_name = 'cartitems'
    template_name='cartitem/list_cartitem.html'

class CreateCartItemView(CreateView):
    model = CartItem
    template_name = 'cartitem/create_cartitem.html'

class UpdateCartItemView(UpdateView):
    model = CartItem
    template_name = 'cartitem/edit_cartitem.html'

class DeleteCartItemView(DeleteView):
    model = Cart
    template_name = 'cartitem/delete_cartitem.html'