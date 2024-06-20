from datetime import date
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField()
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)


    def save(self,*args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Articles(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField()
    content = models.TextField()
    summary = models.CharField(max_length=256)
    featured_image = models.URLField(max_length=512, default="https://dummyimage.com/700x350/343a40/6c757d")
    views_count = models.IntegerField(default=0)
    published = models.BooleanField(default=False)
    published_at = models.DateField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    category = models.ManyToManyField(Category)
    
    def save(self,*args, **kwargs):
        
        if not self.slug:
            self.slug = slugify(self.title)
        
        if not self.published_at and self.published == "True":
            self.published_at = date.today()
        elif self.published == "False":
            self.published_at = None 
        elif not self.published_at and self.published:
            self.published_at = date.today()
            
        super().save(*args, **kwargs)
        
    
    class Meta:
        pass
    
    def __str__(self) :
        return self.title
        