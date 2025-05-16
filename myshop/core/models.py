from django.db import models

# Create your models here.
class OfferProduct(models.Model):
    title=models.CharField(max_length=200)
    desc=models.TextField()
    price=models.DecimalField(max_digits=8, decimal_places=2)
    image=models.ImageField(upload_to="offer_product")

    def __str__(self):
        return self.title
    