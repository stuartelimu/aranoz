from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from shop.models import Item, Order, OrderItem

   
class ItemList(ListView):
    model = Item
    template_name = 'shop/category.html'
    context_object_name = 'items'
    paginate_by = 2


class ItemDetail(DetailView):
    model = Item
    template_name = 'shop/single-product.html'
    context_object_name = 'item'

@login_required
def add_to_cart(request, slug):
    # print(request.GET)
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug = item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.success(request, "This item was updated")
            return redirect("shop:item_detail", item.slug)
        else:
            order.items.add(order_item)
            messages.success(request, "This item was added to your cart")
            return redirect("shop:item_detail", item.slug)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.success(request, "This item was added to your cart")
        return redirect("shop:item_detail", item.slug)


@login_required
def add_single_item_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Item was updated")
            return redirect("shop:cart")


class CartView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {'order': order}
            return render(self.request, 'shop/cart.html', context=context)
        except ObjectDoesNotExist:
            return redirect('/')
