from django import forms
from .models import (
    Recipe,
    Ingredient,
    Measurement,
    Category,
    RecipeIngredient,
    Menu,
)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["title"]
