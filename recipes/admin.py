from django.contrib import admin
from .models import (
    Ingredient,
    Recipe,
    Measurement,
    RecipeIngredient,
    Step,
    RecipeStep,
    Category,
)


# class RecipeInLine(admin.StackedInline):
#     model = RecipeIngredient
#     filter_horizontal = ("ingredient",)


class RecipeInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


class StepInline(admin.TabularInline):
    model = RecipeStep
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["title", "yields", "category"]
    inlines = [RecipeInline, StepInline]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = ["step_number"]


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
