
from django.urls import path

from blog.views import blog_article, blog_home


urlpatterns = [
    path('', blog_home, name="blog_home"),
    path('article/<str:slug>', blog_article, name="article"),

]
