from django.urls import path
from .views import Index, RecipeView


urlpatterns = [
    path('', Index.as_view(), name='home'),
#     path('blog/', views.blog, name='blog'),
    path('recipes/', RecipeView.as_view(), name='recipes')
]