from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product, Category


def product_list(request):
    products = Product.objects.all().order_by("-created_at")
    categories = list(Category.objects.all())

    query = request.GET.get("q", "").strip()
    category_id = request.GET.get("category", "")
    selected = int(category_id) if category_id.isdigit() else None

    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    if selected:
        products = products.filter(category_id=selected)

    for c in categories:
        c.is_selected = c.pk == selected

    return render(
        request,
        "store/product_list.html",
        {
            "products": products,
            "categories": categories,
            "query": query,
            "selected_category": selected,
        },
    )


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "store/product_detail.html", {"product": product})