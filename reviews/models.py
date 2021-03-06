from django.db import models

from products.models import Product
from profiles.models import UserProfile


class Review(models.Model):
    created_by = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    rating_choices = [
        ('One', '1/5'),
        ('Two', '2/5'),
        ('Three', '3/5'),
        ('Four', '4/5'),
        ('Five', '5/5'),
    ]
    rating = models.CharField(
        max_length=5,
        choices=rating_choices,
        default='Five',
    )
