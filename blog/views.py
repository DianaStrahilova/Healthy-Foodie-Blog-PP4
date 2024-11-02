from django.views.generic import TemplateView, ListView, CreateView, DetailView
from .models import Recipe, Comment
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipeForm, CommentForm
from django.http import HttpResponse



# Create your views here.

class Index(TemplateView):
    template_name = 'blog/index.html'


class RecipeView(ListView):
    # model = Recipe
    queryset = Recipe.objects.all()
    template_name = 'blog/recipes.html' 
    context_object_name = 'recipes'
    paginate_by = 6



class RecipeDetail(DetailView):
    """View a single recipe"""

    template_name = "blog/recipe_detail.html"
    model = Recipe

    

class AddRecipe(LoginRequiredMixin, CreateView):
    template_name = 'blog/add_recipe.html'
    model = Recipe
    form_class = RecipeForm
    success_url = '/recipes/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddRecipe, self).form_valid(form)



        

