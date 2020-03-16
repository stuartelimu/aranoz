from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from shop.models import Item

class IndexView(TemplateView):
    template_name = 'index.html'
   

class ItemList(ListView):
    model = Item
    template_name = 'shop/category.html'
    context_object_name = 'items'