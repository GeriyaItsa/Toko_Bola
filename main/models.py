import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('pakaian', 'Pakaian'),
        ('aksesoris', 'Aksesoris'),
        ('sepatu', 'Sepatu'),
        ('bola', 'Bola')
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    thumbnail = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.title
    