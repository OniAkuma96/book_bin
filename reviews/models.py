from django.db import models

from products.models import Product
from profiles.models import UserProfile


class Review(models.Model):
    created_by = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    rating = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.created_by
