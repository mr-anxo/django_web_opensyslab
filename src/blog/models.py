from datetime import date
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)


class Articles(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    summary = models.CharField(max_length=256)
    featured_image = models.URLField(max_length=512, default="https://user-images.githubusercontent.com/24848110/33519396-7e56363c-d79d-11e7-969b-09782f5ccbab.png")
    views_count = models.IntegerField(default=0)
    published = models.BooleanField(default=False)
    published_at = models.DateField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    category = models.ManyToManyField(Category)
    
    def save(self,*args, **kwargs):
        
        if not self.slug:
            self.slug = slugify(self.title)
        
        if not self.published_at and self.published:
            self.published_at = date.today()
        super().save(*args, **kwargs)