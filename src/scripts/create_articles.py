import json
from blog.models import Articles

with open("scripts/blog-articles.json","r") as file:
    data = json.load(file)

for bp in data:
    Articles.objects.create(title=bp["title"],
                            slug=bp["slug"],
                            published=bp["published"],
                            content=bp["content"],
                            summary=bp["summary"],
                            featured_image=bp["featured_image"])