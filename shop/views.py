from django.shortcuts import render
from django.views.generic import TemplateView
from items.models import Item

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