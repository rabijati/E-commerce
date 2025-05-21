from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('shop/',shop,name="shop"),
    path('productdetail/<int:id>',product_details,name="product_details"),
    path('checkout/',checkout,name="checkout"),
    path('cart/',cart,name="cart"),
    path('blog/',blog,name="blog"),
    path('blogsingle/',blogSingle,name="blogsingle"),
    path('error/',error,name="error"),
    path('contact/',contact,name="contact"),
]
