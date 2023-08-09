from django.db import models

# Create your models here.
class OrganicStoreModel(models.Model):
    CATEGORY = [
        ('Vegetables','Vegetables'),
        ('Fruits','Fruits'),
        ('Dairy','Dairy'),
        ('Meat','Meat'),
        ('Fish & SeaFood','Fish & SeaFood'),
    ]
    id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=30)
    farmer_name = models.CharField(max_length=20)
    category = models.CharField(max_length=30,choices=CATEGORY)
    collected_food = models.DateTimeField(auto_now_add=True)
    last_collected = models.DateTimeField(auto_now = True)
    