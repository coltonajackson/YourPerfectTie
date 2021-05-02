from django.shortcuts import render
from django.views.generic import TemplateView
from items.models import Item
from cart.cart import Cart
from items.models import Item

def add_to_cart(request, item_id):
    item = Item.objects.get(id=item_id)
    cart = Cart(request)
    cart.add(item, item.current_price, 1)
    return render(request, 'cart.html')

def remove_from_cart(request, product_id):
    item = Item.objects.get(id=item_id)
    cart = Cart(request)
    cart.remove(item)
    return render(request, 'cart.html')
	
def get_cart(request):
    return render(request, 'cart.html', {'cart': Cart(request)})

def index(request):
	all_items = Item.objects.all()
	context = {
		'all_items': all_items,
	}
	return render(request, 'index.html', context=context)
'''
class HomePageView(TemplateView):
	all_items = Item.objects.all()
	template_name = 'index.html'
'''
class CartPageView(TemplateView):
	template_name = 'cart.html'