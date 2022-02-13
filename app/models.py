from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    name= models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True, unique=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default='profile.svg')

    REQUIRED_FIELDS = []



class Category(models.Model):
    choices = (
    ('M', 'male'),
    ('F', 'female'),
    ('Uni', 'unisex')
    )
    name =  models.CharField(max_length=10, choices=choices, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):    
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        index_together = ( ('id', 'slug'),)

    def __str__(self):
        return self.name 