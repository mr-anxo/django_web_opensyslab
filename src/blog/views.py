from django.shortcuts import render
from blog.models import Articles, Category

# Create your views here.

def blog_home(request):
    articles = Articles.objects.filter(published=True)
    categories = Category.objects.all()
    return render(request, "blog-home.html", context={ "articles" : articles, "categories" : categories })


def blog_article(request, article_slug):
    article = Articles.objects.get(slug=article_slug)
    
    if article.slug:
        return render(request, f"blog-post.html", context={ "article" : article})
    else:
        return render(request, "404.html")