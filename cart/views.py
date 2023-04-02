from django.shortcuts import render, redirect

# Create your views here.

def view_cart(request):
    """ View to show cart """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    cart[item_id] = int(1)

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)