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

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created_at",
    )
