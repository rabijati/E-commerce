from django.db import models

# Create your models here.
class OfferProduct(models.Model):
    title=models.CharField(max_length=200)
    desc=models.TextField()
    price=models.DecimalField(max_digits=8, decimal_places=2)
    image=models.ImageField(upload_to="offer_product")

    def __str__(self):
        return self.title

class Category(models.Model):
    title=models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
class Brand(models.Model):
    title=models.CharField(max_length=200)

    def __str__(self):
        return self.title
    

class SubCategory(models.Model):
    title=models.CharField(max_length=200)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} + {self.category.title}"
    
class Product(models.Model):
    name=models.CharField(max_length=200)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory=models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand, on_delete=models.CASCADE,null=True)
    desc=models.TextField()
    image=models.ImageField(upload_to="product_image")
    image2=models.ImageField(upload_to="product_image")
    image3=models.ImageField(upload_to="product_image")
    mark_price=models.DecimalField(max_digits=8, decimal_places=2)
    discount_percentage=models.DecimalField(max_digits=4, decimal_places=2)
    price=models.DecimalField(max_digits=8, decimal_places=2, editable=False)
    created_date=models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.price=self.mark_price*(1-self.discount_percentage/100)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
