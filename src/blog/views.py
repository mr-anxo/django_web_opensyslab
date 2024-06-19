from django.shortcuts import render

from blog.models import Articles

# Create your views here.

def blog_home(request):
    articles = Articles.objects.filter(published=True)
    return render(request, "blog-home.html", context={ "articles" : articles })


def blog_article(request, article_slug):
    article = Articles.objects.get(slug=article_slug)
    
    if article.slug:
        return render(request, f"blog-post.html", context={ "article" : article})
    else:
        return render(request, "404.html")