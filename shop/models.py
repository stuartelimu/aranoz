from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings
from taggit.managers import TaggableManager

User = get_user_model()


class Item(models.Model):

    AVAILABILITY_CHOICES = [
        ('IS', 'In Stock'),
        ('OS', 'Out Of Stock')
    ]

    title = models.CharField(max_length=120)
    price = models.FloatField()
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    availability = models.CharField(max_length=2, choices=AVAILABILITY_CHOICES, default='IS')
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop:item_detail', args=[self.slug])


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.item.title

    
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    created_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username





