from django.contrib import admin
from blog.models import Articles, Category

# Register your models here.

@admin.register(Articles)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "slug",
        "published",
        "author",
    )
    search_fields = ("title",)
    list_filter = ("published", "author")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created_at",
    )
    
    search_fields = ("name",)
    list_filter = ("name",)
