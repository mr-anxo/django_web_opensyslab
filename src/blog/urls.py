
from django.urls import path

from blog.views import blog_home


urlpatterns = [
    path('', blog_home, name="blog_home"),
]
