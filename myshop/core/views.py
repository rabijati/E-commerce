from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.db.models import Count
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    offer=OfferProduct.objects.all()
    cate=Category.objects.all()
    br=Brand.objects.annotate(product_count=Count('product'))

    cateid=request.GET.get('category')
    brid=request.GET.get('brand')
    if cateid and brid:
        product=Product.objects.filter(subcategory=cateid, brand=brid)
    elif cateid:
        product=Product.objects.filter(subcategory=cateid)
    else:
        product=Product.objects.all()

    paginator=Paginator(product,9)
    num_p=request.GET.get('page')
    data=paginator.get_page(num_p)
    total=data.paginator.num_pages

    context={
        'offer':offer,
        'cate':cate,
        'product':product,
        'br':br,    
        'data':data,
        'num':[i+1 for i in range(total)],
    
    }
    return render(request,'main/index.html',context)





def product_details(request, id):
    data=get_object_or_404(Product,id=id)
    return render(request,'main/product-details.html',{"data":data})


def shop(request):
    return render(request,'main/shop.html')
def checkout(request):
    return render(request,'main/checkout.html')
def cart(request):
    return render(request,'main/cart.html')
def blog(request):
    return render(request,'main/blog.html')
def blogSingle(request):
    return render(request,'main/blog-single.html')
def error(request):
    return render(request,'main/404.html')
def contact(request):
    return render(request,'main/contact-us.html')