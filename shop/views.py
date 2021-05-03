from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from carton.cart import Cart
from products.models import Product

# def index(request):
# 	all_products = Product.objects.all()
# 	context = {
# 		'all_products': all_products,
# 	}
# 	return render(request, 'index.html', context=context)

# def add_to_cart(request):
#     cart = Cart(request.session)
#     product = Product.objects.get(id=request.GET.get('product_id'))
#     cart.add(product, price=product.price)
#     return HttpResponse("Added")

# class HomePageView(TemplateView):
# 	template_name = 'index.html'

class HomePageView(ListView):
	model = Product
	template_name = 'index.html'

class CartPageView(TemplateView):
	template_name = 'cart.html'