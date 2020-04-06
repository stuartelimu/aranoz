from django.urls import path
from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.ItemList.as_view(), name='item_list'),
    path('<slug:slug>/', views.ItemDetail.as_view(), name='item_detail'),
]