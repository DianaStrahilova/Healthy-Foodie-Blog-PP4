from django.urls import path
from . import views
from .views import Index, RecipeView, RecipeDetail, AddRecipe
from django.views import generic


urlpatterns = [
   
    path('', Index.as_view(), name='home'),
    path('recipes/', RecipeView.as_view(), name='recipes'),
    path('<slug:slug>', RecipeDetail.as_view(), name='recipe'),
    path('add_recipe/', AddRecipe.as_view(), name='add_recipe'),
    
   
    
      
    
]