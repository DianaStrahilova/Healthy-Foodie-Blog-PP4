from django.urls import path
from .views import Index, RecipeView
from . import views
from django.views import generic


urlpatterns = [
    path('', Index.as_view(), name='home'),
    # path('blog/', views.blog, name='blog'),
    path('recipes/', RecipeView.as_view(), name='recipes')
]