from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_user, name="login"),
    path("logout", views.logout_user , name = "logout"),
    path("register", views.register_user , name = "register"),
    path("myorder", views.myorder , name = "myorder"),
    path("orders", views.orders , name = "orders")
]
