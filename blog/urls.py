from django.urls import path
from . import views
from .views import Index, RecipeView, recipe_detail, AddRecipe
from django.views import generic


urlpatterns = [
   
    path('', Index.as_view(), name='home'),
    path('recipes/', RecipeView.as_view(), name='recipes'),
    path('<slug:slug>', views.recipe_detail, name='recipe'),
    path('add_recipe/', AddRecipe.as_view(), name='add_recipe'),
    
   
    
      
    
]