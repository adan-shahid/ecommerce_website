from .models import Cart

def cart_badge_count(request):
    if not request.user.is_authenticated:
        return {'cart_badge_count': 0}    
    try:
        cart = Cart.objects.get(user=request.user)
        total_items = sum(item.quantity for item in cart.items.all())
        # Matche the exact variable name in your template
        return {'cart_badge_count': total_items}
    except Cart.DoesNotExist:
        return {'cart_badge_count': 0}