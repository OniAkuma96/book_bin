from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Product
from reviews.models import Review
from .forms import ProductForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    genre = None

    if request.GET:
        if 'genre' in request.GET:
            genre = request.GET['genre']
            products = products.filter(main_genre__in=genre)

        if 'q' in request.GET:
            query = request.GET['q']
            # if not query:
            #     messages.error(request, "You didn't enter any search criteria!")
            #     return redirect(reverse('products'))
        
            queries = (
                Q(title__icontains=query) | Q(author__icontains=query) | Q(sub_genre__icontains=query)
            )
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'genre': genre,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show details of an individual product """
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.all()

    context = {
        'product': product,
        'reviews': reviews,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ Add a product to the store """
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
