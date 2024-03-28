from django.urls import path

from . import views

# directory list
urlpatterns = [
    path("home", views.index, name="home"),
    path("products", views.products, name="products"),
    path("shop", views.shop, name="shop"),
    path("user_login", views.user_login, name="user_login"),
    path("user_register", views.user_register, name="user_register")
]
