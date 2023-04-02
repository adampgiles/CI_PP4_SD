from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from developers.models import Developer
# Create your views here.

def view_cart(request):
    """ View to show cart """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add item to the shopping cart """

    developer = get_object_or_404(Developer, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    cart[item_id] = int(1)

    request.session['cart'] = cart

    messages.success(request, f'{developer.profile_name} - £{developer.price} added to cart')
    return redirect(redirect_url)

def remove_from_cart(request, item_id):
    """ Remove item from the shopping cart """

    developer = get_object_or_404(Developer, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    cart.pop(item_id)

    request.session['cart'] = cart

    messages.success(request, f'{developer.profile_name} - £{developer.price} removed from cart')
    return redirect(redirect_url)