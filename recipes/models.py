from pyexpat import model
from tkinter import CASCADE
from django.db import models


class UnitModel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    class Meta:
        verbose_name = "Unidades de Medida"

    def __str__(self):
        return self.name


class IngredientModel(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Ingrediente"
        
    def __str__(self):
        return self.name

class RecipeTypeModel(models.Model):
    name=models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.name

class RecipeModel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    instructions = models.TextField()
    prep_time = models.PositiveIntegerField(help_text="Time in minutes")
    cook_time = models.PositiveIntegerField(help_text="Time in minutes")
    servings = models.PositiveIntegerField()
    type = models.ForeignKey(RecipeTypeModel, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Receta"

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        RecipeModel, on_delete=models.CASCADE, related_name="ingredients"
    )
    ingredient = models.ForeignKey(IngredientModel, on_delete=models.CASCADE)
    unit = models.ForeignKey(UnitModel, on_delete=models.SET_NULL, null=True)
    quantity = models.FloatField()

        
    def __str__(self):
        return f"{int(self.quantity)} {self.unit} de {self.ingredient}"
