def cart_counter(request):
    cart = request.session.get('cart', {})
    total_itms = sum(int(qty) for qty in cart.values())
    return {'cart_itms_count':total_itms}