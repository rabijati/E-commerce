from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'main/index.html')
def shop(request):
    return render(request,'main/shop.html')
def productDetails(request):
    return render(request,'main/product-details.html')
def checkout(request):
    return render(request,'main/checkout.html')
def cart(request):
    return render(request,'main/cart.html')
def login(request):
    return render(request,'auth/login.html')
def blog(request):
    return render(request,'main/blog.html')
def blogSingle(request):
    return render(request,'main/blog-single.html')
def error(request):
    return render(request,'main/404.html')
def contact(request):
    return render(request,'main/contact-us.html')