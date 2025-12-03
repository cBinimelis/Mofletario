from django.shortcuts import render
from .models import RecipeModel, RecipeIngredient
from recipes.forms import RecipeForm

# Create your views here.
def home(request):
    return render(request, "index.html")


def list(request):
    if request.method == "GET":
        recipes = RecipeModel.objects.all()
        context = {"recipes": recipes}
    if request.method =='POST':
        value = request.POST.__getitem__("searchRecipe")
        recipes= RecipeModel.objects.filter(name__icontains=value)
        context = {"recipes": recipes}
    return render(request, "recipes/recipes/list.html", context)


def view(request, pk):
    recipe = RecipeModel.objects.get(id=pk)
    ingredients = RecipeIngredient.objects.filter(recipe=recipe.id)
    context = {"recipe": recipe, "ingredients": ingredients}
    return render(request, "recipes/recipes/view.html", context)


def edit(request, pk):
    print("")


def delete(request, pk):
    print("")


def create(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        form.save()
        # messages.success(request, "Receta creada")
        return redirect("recipes:list")
    else:
        form = RecipeForm()
    context = {"form": form}
    return render(request, "recipes/recipes/form.html", context)
