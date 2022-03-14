from django.urls import path
from stock_profit_calculator import views

urlpatterns = [
    path("", views.home, name="home"),
    path("stock/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path('post/ajax/stock', views.postStock, name = "post_stock"),
]