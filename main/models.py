from django.db import models
from django.contrib.auth.models import User

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
        ('lain', 'Lainnya'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # tambahkan ini
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    rating = models.FloatField(null=True, blank=True)
    brand = models.CharField(max_length=100, blank=True)

 
    def __str__(self):
        return self.name
    
    
 