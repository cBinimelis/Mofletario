from django.contrib import admin
from .models import Ingredient, Recipe


# Register your models here.
class IngredientInLine(admin.TabularInline):
    model = Recipe.ingredients.through
    extra = 1


@admin.register(Recipe)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "yields"]
    inlines = [IngredientInLine]
