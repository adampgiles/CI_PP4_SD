from django.shortcuts import render

# Create your views here.

def view_cart(request):
    """ View to show cart """

    return render(request, 'cart/cart.html')