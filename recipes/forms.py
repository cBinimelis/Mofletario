from django import forms
from .models import (
    RecipeModel,
)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeModel
        fields = [
            "name",
        ]

#    CHOICES =[('desayuno','Desayuno')('almuerzo','Almuerzo'),('cena','Cena'),('aperitivo','Aperitivo'),('postre','Postre')]