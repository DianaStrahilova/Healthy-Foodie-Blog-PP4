from django.urls import path
from . import views
from .views import Index, RecipeView, recipe_detail, AddRecipe
from django.views import generic


urlpatterns = [

    path('', Index.as_view(), name='home'),
    path('add_recipe/', AddRecipe.as_view(), name='add_recipe'),
    path('recipes/', RecipeView.as_view(), name='recipes'),
    path('<slug:slug>/', views.recipe_detail, name='recipe'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
     
    
]
    
   
    
      
    