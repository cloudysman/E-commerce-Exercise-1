from django.db import models
from book.models import Book

class Cart(models.Model):
    
    cart_id = models.AutoField(primary_key=True)
    date_added = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

# Create your models here.
