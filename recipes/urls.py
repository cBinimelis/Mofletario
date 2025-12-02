from django.urls import path
from . import views

app_name = "recipes"

urlpatterns = [
    path("", views.home, name="home"),
    path("recipes/", views.list, name="list"),
    path("recipes/create", views.create, name="create"),
    path("recipes/<int:pk>", views.view, name="view"),
    path("recipes/<int:pk>/edit", views.edit, name="edit"),
    path("recipes/<int:pk>/delete", views.delete, name="delete"),
]
