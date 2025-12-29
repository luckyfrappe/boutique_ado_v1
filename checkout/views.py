from django.contrib import messages
from django.shortcuts import render, reverse, redirect

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request,
                       "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51SgsoY4K4yibvJ9oSngQExpPa7NoQuKNcdm6SWivaPe5ZIf8Zx1EL4kkGG23YHdyCVpeoEnZRNYyEI7UQYCDy60X0066nJGQ1Z',
        'client_secret': 'test client secret'
    }
    return render(request, template, context)
