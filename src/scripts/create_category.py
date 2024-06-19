from blog.models import Category

categories = ["Programmation", "Système d'exploitation", "Python", "Linux", "Réseaux informatiques", "Système", "Technos"]
created_categories = Category.objects.values_list("name",flat=True)

for item in categories:
    if item not in created_categories:
        cat = Category(name=item)
        cat.save()