from django.db import models


class RecipeStep(models.Model):
    step_number = models.IntegerField()
    instruction = models.TextField(max_length=1000)


class Category(models.Model):
    name = models.CharField(max_length=50)


class Measurement(models.Model):
    name = models.CharField(max_length=30)
    abbreviation = models.CharField(max_length=10)

    def __str__(self):
        return self.abbreviation


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    amount = models.IntegerField()
    measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    preparation_time = models.IntegerField()
    cook_time = models.IntegerField()
    ready_in = models.IntegerField()
    yields = models.IntegerField()
    calories_ps = models.IntegerField(null=True)
    image = models.ImageField(null=True, upload_to="recipes")
    ingredients = models.ManyToManyField(Ingredient)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    recipe_step = models.ForeignKey(RecipeStep, on_delete=models.CASCADE, null=True)


class Menu(models.Model):
    name = models.CharField(max_length=50)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
