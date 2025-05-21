from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([OfferProduct,Category,SubCategory,Product,Brand])
