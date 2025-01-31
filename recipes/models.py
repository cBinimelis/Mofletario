from django.db import models


class RecipeStep(models.Model):
    step_number = models.IntegerField()
    instruction = models.TextField(max_length=1000)


class Category(models.Model):
    name = models.CharField(max_length=50)


class Measurement(models.Model):
    name = models.CharField(max_length=30)
    abbreviation = models.CharField(max_length=10)


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE)


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    preparation_time = models.IntegerField()
    cook_time = models.IntegerField()
    ready_in = models.IntegerField()
    yields = models.IntegerField()
    calories_ps = models.IntegerField(null=True)
    image = models.ImageField(null=True, upload_to='recipes')
    ingredients = models.ManyToManyField("Ingredient", through="RecipeIngredient")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    recipe_step = models.ForeignKey(RecipeStep, on_delete=models.CASCADE)


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.IntegerField()


class Menu(models.Model):
    name = models.CharField(max_length=50)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
