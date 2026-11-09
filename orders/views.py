from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import transaction
from cart.models import Cart
from store.models import Product
from .forms import CheckoutForm
from .models import Order, OrderItem


@login_required
def checkout(request):
    cart = Cart.objects.filter(user=request.user).first()
    if not cart or not cart.items.exists():
        return redirect("cart_detail")

    error = None

    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                items = list(cart.items.select_related("product"))
                products = {
                    p.pk: p
                    for p in Product.objects.select_for_update().filter(
                        pk__in=[i.product_id for i in items]
                    )
                }

                for item in items:
                    product = products[item.product_id]
                    if item.quantity > product.stock:
                        error = f"Sorry, only {product.stock} of {product.name} left in stock."
                        break

                if error is None:
                    order = form.save(commit=False)
                    order.user = request.user
                    order.total = cart.total_price()
                    order.payment_method = "Cash on Delivery"
                    order.save()
                    for item in items:
                        product = products[item.product_id]
                        OrderItem.objects.create(
                            order=order,
                            product=product,
                            quantity=item.quantity,
                            price=product.price,
                        )
                        product.stock -= item.quantity
                        product.save()
                    cart.items.all().delete()
                    return redirect("order_detail", order_id=order.pk)
    else:
        form = CheckoutForm()

    return render(
        request,
        "orders/checkout.html",
        {"form": form, "cart": cart, "error": error},
    )


@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "orders/order_list.html", {"orders": orders})


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id, user=request.user)
    return render(request, "orders/order_detail.html", {"order": order})