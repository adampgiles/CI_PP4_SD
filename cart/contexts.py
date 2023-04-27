from django.shortcuts import get_object_or_404
from developers.models import Developer


def cart_contents(request):
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        developer = get_object_or_404(Developer, pk=item_id)
        total += developer.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'developer': developer,
        })
    context = {
        'cart_items': cart_items,
        'total': total,
    }

    return context
