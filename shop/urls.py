from django.urls import path
from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.ItemList.as_view(), name='item_list'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('<slug:slug>/', views.ItemDetail.as_view(), name='item_detail'),
    path('add/<slug:slug>/', views.add_to_cart, name='add_to_cart'),
    path('add_single_item_to_cart/<slug:slug>/', views.add_single_item_to_cart, name='add_single_item_to_cart'),

]