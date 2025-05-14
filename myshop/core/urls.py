from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('shop/',shop,name="shop"),
    path('productdetails/',productDetails,name="product-details"),
    path('checkout/',checkout,name="checkout"),
    path('cart/',cart,name="cart"),
    path('login/',login,name="login"),
    path('blog/',blog,name="blog"),
    path('blogsingle/',blogSingle,name="blogsingle"),
    path('error/',error,name="error"),
    path('contact/',contact,name="contact"),
]
