from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from store.models import Product
from .models import Cart, CartItem


@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, "cart/cart_detail.html", {"cart": cart})


@login_required
def add_to_cart(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not item_created:
            item.quantity += 1
            item.save()
    return redirect("cart_detail")


@login_required
def remove_from_cart(request, item_id):
    if request.method == "POST":
        item = get_object_or_404(CartItem, pk=item_id, cart__user=request.user)
        item.delete()
    return redirect("cart_detail")




@login_required
def update_quantity(request, item_id):
    if request.method == "POST":
        item = get_object_or_404(CartItem, pk=item_id, cart__user=request.user)
        action = request.POST.get("action")
        if action == "increase":
            if item.quantity < item.product.stock:
                item.quantity += 1
                item.save()
        elif action == "decrease":
            if item.quantity > 1:
                item.quantity -= 1
                item.save()
            else:
                item.delete()
    return redirect("cart_detail")    