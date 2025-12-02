from django.contrib import admin
from .models import RecipeModel, IngredientModel, UnitModel, RecipeIngredient,RecipeTypeModel


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]


admin.site.register(RecipeModel, RecipeAdmin)
admin.site.register(RecipeTypeModel)
admin.site.register(IngredientModel)
admin.site.register(UnitModel)
