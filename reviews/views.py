from django.shortcuts import render, get_object_or_404
from products.models import Product


def reviews(request, product_id):
    """ A view to show all reviews of a product """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'reviews/reviews.html', context)
