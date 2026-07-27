from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # path("signup/", views.signup, name="signup"),
    path("product_details/<slug:slug>/<int:id>/", views.product_details, name="product_details")
]