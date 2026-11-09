from django.urls import path
from . import views

urlpatterns = [
    path("", views.order_list, name="order_list"),
    path("checkout/", views.checkout, name="checkout"),
    path("<int:order_id>/", views.order_detail, name="order_detail"),
]