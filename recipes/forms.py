from django import forms
from .models import (
    Recipe,
    Ingredient,
    Measurement,
    RecipeStep,
    Category,
    RecipeIngredient,
    Menu,
)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["title"]
