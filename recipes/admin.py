from django.contrib import admin
from .models import Ingredient, Recipe, Measurement


# Register your models here.
# class IngredientInLine(admin.TabularInline):
#     model = Recipe.ingredients.through
#     extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["title", "yields"]
    # inlines = [IngredientInLine]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ["name"]
