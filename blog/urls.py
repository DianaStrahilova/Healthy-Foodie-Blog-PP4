from . import views
from django.urls import path
from .views import Index, RecipeView, AddRecipe, EditRecipe, DeleteRecipe
from django.views import generic


urlpatterns = [
     path('', Index.as_view(), name='home'),
     path('add_recipe/', AddRecipe.as_view(), name='add_recipe'),
     path('recipes/', RecipeView.as_view(), name='recipes'),
     path('<slug:slug>/edit_recipe', EditRecipe.as_view(), name='edit_recipe'),
     path('<slug:slug>/delete_recipe', DeleteRecipe.as_view(), name='delete_recipe'),
     path('<slug:slug>/', views.recipe_detail, name='recipe'),
     path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
     path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
     
     
    
]
    
   
    
      
    