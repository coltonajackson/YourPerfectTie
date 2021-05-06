from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView, DeleteView
from products.models import Product
from .models import Cart, CartItem

class CartTemplateView(TemplateView):
    model = Cart
    template_name='cart.html'

##-------------- Cart Views --------------------------------------
class CartDetailView(DetailView):
    model = Cart
    template_name='cart/cart_detail.html'

class CartListView(ListView):
    model = Cart
    context_object_name = 'carts'
    template_name='cart/cart_list.html'

class CartCreateView(CreateView):
    model = Cart
    template_name = 'cart/cart_new.html'

class CartUpdateView(UpdateView):
    model = Cart
    template_name = 'cart/cart_edit.html'

class CartDeleteView(DeleteView):
    model = Cart
    template_name = 'cart/cart_delete.html'


##-------------- CartItem Views --------------------------------------
class CartItemDetailView(DetailView):
    model = CartItem
    template_name='cartitem/cartitem_detail.html'

class CartItemListView(ListView):
    model = CartItem
    context_object_name = 'cartitems'
    template_name='cartitem/cartitem_list.html'

class CartItemCreateView(CreateView):
    model = CartItem
    template_name = 'cartitem/cartitem_new.html'

class CartItemUpdateView(UpdateView):
    model = CartItem
    template_name = 'cartitem/cartitem_edit.html'

class CartItemDeleteView(DeleteView):
    model = Cart
    template_name = 'cartitem/cartitem_delete.html'