from django.urls import path
from shop import views
from django.views.generic import TemplateView

app_name = 'shop'

urlpatterns = [
    path('', views.ItemList.as_view(), name='item_list'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('checkout/', TemplateView.as_view(template_name='shop/checkout.html'), name='checkout'),
    path('<slug:slug>/', views.ItemDetail.as_view(), name='item_detail'),
    path('add/<slug:slug>/', views.add_to_cart, name='add_to_cart'),
    path('add_single_item_to_cart/<slug:slug>/', views.add_single_item_to_cart, name='add_single_item_to_cart'),
    path('remove_single_item_from_cart/<slug:slug>/', views.remove_single_item_from_cart, name='remove_single_item_from_cart'),

]