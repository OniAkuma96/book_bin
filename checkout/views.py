from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JddoMFHhgdOK0dN17van7D3Vm9BvlznJgiwxWR9bHAtAR8M41wSC18hwOIDLuiHnd5aUZ2sIHiE4fAyfrzn6Eaw00roFWfBEn',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
