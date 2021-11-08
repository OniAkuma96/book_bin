from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from products.models import Product
from .forms import NewReviewForm


# def new_review(request, product_id):
#     if request.method == 'POST':
#         form = NewReviewForm()
#         if form.is_valid():
#             product = form.save()
#             messages.success(request, 'Successfully added review!')
#             return redirect(reverse('product_detail', args=[product.id]))
#         else:
#             messages.error(request, 'Failed to add review. Please ensure the form is valid.')
#     else:
#         form = NewReviewForm()

#     product = get_object_or_404(Product, pk=product_id)

#     context = {
#         'product': product,
#         'form': form,
#     }

#     return render(request, 'reviews/new_review.html', context)


def new_review(request, product_id):
    if request.method == 'POST':
        form = NewReviewForm()
        if form.is_valid:
            product = get_object_or_404(Product, pk=product_id)
            form.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add review. Please ensure the form is valid.')

    else:
        form = NewReviewForm()

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
        'form': form,
    }

    return render(request, 'reviews/new_review.html', context)
