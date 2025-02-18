from io import BytesIO
from PIL import Image
from django.db import models
from django.core.files.base import ContentFile


class Step(models.Model):
    step_number = models.IntegerField()

    def __str__(self):
        return f"{self.step_number}"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Measurement(models.Model):
    name = models.CharField(max_length=30)
    abbreviation = models.CharField(max_length=10)

    def __str__(self):
        return self.abbreviation


class Ingredient(models.Model):
    name = models.CharField(max_length=250)

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
    image = models.ImageField(null=True, upload_to="static/img/recipes")
    ingredients = models.ManyToManyField(
        Ingredient, through="RecipeIngredient", blank=True
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    steps = models.ManyToManyField(Step, through="RecipeStep", blank=True)

    def save(self, *args, **kwargs):
        title = self.title.replace(" ", "").lower()
        image = Image.open(self.image)

        new_width = 500
        original_width, original_height = image.size
        new_height = int((new_width / original_width) * original_height)
        image = image.resize((new_width, new_height), Image.LANCZOS)
        temp_img = BytesIO()
        image.save(temp_img, format="JPEG", quality=70, optimize=True)
        temp_img.seek(0)
        img_name = f"{title}.jpg"
        self.image.save(img_name, ContentFile(temp_img.read()), save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    amount = models.IntegerField()
    measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE)
    instructions = models.CharField(max_length=100, blank=True)


class RecipeStep(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    step = models.ForeignKey(Step, on_delete=models.CASCADE)

    instruction = models.CharField(max_length=1000)


class Menu(models.Model):
    name = models.CharField(max_length=50)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
