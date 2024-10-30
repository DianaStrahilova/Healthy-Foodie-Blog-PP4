from django.views.generic import TemplateView, ListView
from .models import Recipe
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic



# Create your views here.

class Index(TemplateView):
    template_name = 'blog/index.html'

class RecipeView(generic.ListView):
    # model = Recipe
    queryset = Recipe.objects.all()
    template_name = 'blog/recipes.html' 

# def recipe_list(request):
#     queryset = Recipe.objects.all()
#     # recipes = Recipe.objects.all()
#     return render(request, 'blog/recipes.html')

def recipe_detail(request, slug):
    recipe = Recipe.objects.get(slug=slug)
    return render(request, 'blog/recipe_detail.html', {'recipe': recipe})
