from django.shortcuts import render, get_object_or_404
from products.models import Product

def new_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'reviews/new_review.html', context)
