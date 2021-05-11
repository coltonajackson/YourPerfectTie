from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView
# from carton.cart import Cart
from products.models import Product
from categories.models import Category
# import os, stripe

# This is your real test secret API key.
# stripe.api_key = settings.STRIPE_SECRET_KEY


def index(request):
	all_products = Product.objects.all()
	all_categories = Category.objects.all()
	context = {
		'all_products': all_products,
		'all_categories': all_categories,
	}
	return render(request, 'index.html', context=context)

def featured_items(request):
	return render(request, 'shop/featured_items.html')

def category_items(request, pk):
	all_products = Product.objects.all()
	all_categories = Category.objects.all()
	filtered_products = Product.objects.filter(category_id=pk)
	selected_category = Category.objects.get(id=pk)
	context = {
		'all_products': all_products,
		'all_categories': all_categories,
		'filtered_products': filtered_products,
		'selected_category': selected_category,
	}
	return render(request, 'shop/category_items.html', context=context)

# class HomePageView(TemplateView):
# 	template_name = 'index.html'

# class HomePageView(ListView):
# 	model = Product
# 	template_name = 'index.html'

	# def get_context_data(self, **kwargs):
	# 	product = Product.objects.get(id=1)
	# 	context = super(HomePageView, self).get_context_data(**kwargs)
	# 	context.udpate({
	# 		'product': product,
	# 		'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
	# 	})
	# 	return context

# class CreateCheckoutSessionView(View):
# 	def post(self, request, *args, **kwargs):
# 		# Domain Name for project
# 		YOUR_DOMAIN = 'http://127.0.0.1:8888'
# 		checkout_session = stripe.checkout.Session.create(
# 			payment_method_types = ['card'],
# 			line_items = [
# 				{
# 					'price_data': {
# 						'currency': 'usd',
# 						'unit_amount': 2000,
# 						'product_data': {
# 							'name': 'Stubborn Attachments',
# 						},
# 					},
# 					'quantity': 1,
# 				},
# 			],
# 			mode = 'payment',
# 			success_url = YOUR_DOMAIN + '/success.html',
# 			cancel_url = YOUR_DOMAIN + '/cancel.html',
# 		)
# 		return JsonResponse({
# 			'id': checkout_session.id,
# 		})
