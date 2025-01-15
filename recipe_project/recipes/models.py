from django.db import models

class Category(models.Model):
       name = models.CharField(max_length=100)

       def __str__(self):
           return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='recipes', on_delete=models.CASCADE)
    ingredients = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return self.title
