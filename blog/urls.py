from django.urls import path
from . import views
from .views import Index, recipe_detail, RecipeView
from django.views import generic


urlpatterns = [
    path('', Index.as_view(), name='home'),
    # path('blog/', views.blog, name='blog'),
    # path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('recipes/', RecipeView.as_view(), name='recipes'),
    path('<slug:slug>/', views.recipe_detail, name='recipe'),
    
]