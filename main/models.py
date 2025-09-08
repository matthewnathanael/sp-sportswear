import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('sweater', 'Sweater'),
        ('baju', 'Baju'),
        ('celana', 'Celana'),
        ('sepatu', 'Sepatu'),
        ('tas', 'Tas'),
        ('sleeve', 'Sleeves'),
        ('kaos kaki', 'Kaos Kaki'),
        ('tidak ada', 'Tidak Ada'),
    ]
    

    name = models.CharField
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
    
 
   