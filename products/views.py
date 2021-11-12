from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from reviews.models import Review
from .models import Product
from .forms import ProductForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    main_genre = None

    if request.GET:
        if 'main_genre' in request.GET:
            main_genre = request.GET['main_genre']
            if main_genre == 'fiction':
                products = products.filter(main_genre='Fiction')
            elif main_genre == 'non-fiction':
                products = products.filter(main_genre='Non-Fiction')
            else:
                products = products.filter(main_genre='Children and Young Adult')
            

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
        
            queries = (
                Q(title__icontains=query) | Q(author__icontains=query) | Q(sub_genre__icontains=query)
            )
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'main_genre': main_genre,
    }

    return render(request, 'products/products.html', context)


def calculate_product_rating(product_id):
    overall_rating = 0
    all_reviews = Review.objects.all()
    reviews = all_reviews.filter(product=product_id)
    if reviews:
        for review in reviews:
            if review.rating == 'Five':
                overall_rating += 5
            elif review.rating == 'Four':
                overall_rating += 4
            elif review.rating == 'Three':
                overall_rating += 3
            elif review.rating == 'Two':
                overall_rating += 2
            elif review.rating == 'One':
                overall_rating += 1
        average_rating = overall_rating / len(reviews)
        return average_rating


def product_detail(request, product_id):
    """ A view to show details of an individual product """
    product = get_object_or_404(Product, pk=product_id)
    all_reviews = Review.objects.all()
    reviews = all_reviews.filter(product=product_id)
    average_rating = calculate_product_rating(product_id)

    context = {
        'product': product,
        'reviews': reviews,
        'average_rating': average_rating,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.title}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
