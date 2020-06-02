from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.index, name='index'),
    path("shoplist", views.shoplist, name='shoplist'),
    #path("add", views.add, name='add'),
    #path("dele", views.dele, name='dele'),
    path("cartitems", views.cartitems, name='cartitems'),
    path("proceed", views.proceed, name='proceed'),
    path("submit", views.submit, name='submit'),
]