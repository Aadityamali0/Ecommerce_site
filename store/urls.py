from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # path("signup/", views.signup, name="signup"),
    path("product_details/", views.product_details, name="product_details")
]