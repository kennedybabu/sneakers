from django.db import models

# Create your models here.


class Shoe(models.Model):
    choices = (
        ('M', 'male'),
        ('F', 'female'),
        ('Uni', 'unisex')
    )
    
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    gender = models.CharField(max_length=10, choices=choices, null=True)
    updated = models.DateTimeField(auto_now=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 