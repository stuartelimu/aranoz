from django.shortcuts import render
from django.views.generic import ListView, DetailView
from shop.models import Item


   
class ItemList(ListView):
    model = Item
    template_name = 'shop/category.html'
    context_object_name = 'items'
    paginate_by = 2


class ItemDetail(DetailView):
    model = Item
    template_name = 'shop/single-product.html'
    context_object_name = 'item'