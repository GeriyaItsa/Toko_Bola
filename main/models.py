import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('pakaian', 'Pakaian'),
        ('aksesoris', 'Aksesoris'),
        ('sepatu', 'Sepatu'),
        ('bola', 'Bola')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    thumbnail = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    
    def __str__(self):
        return self.title