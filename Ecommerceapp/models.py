from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,default='uncategorized')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    Category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='Categories')
    product_name = models.CharField(max_length=100)
    desc = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.product_name
