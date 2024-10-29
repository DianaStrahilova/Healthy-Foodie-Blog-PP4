# from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import generic
from django.views.generic import ListView
from .models import Recipe



# Create your views here.
# def home(request):
#     return HttpResponse("This is the home page")

# def blog(request):
#     return HttpResponse("This is my Blog")

class Index(TemplateView):
    template_name = 'blog/index.html'

# class RecipeView(ListView):
#     model = Recipe
#     template_name = 'blog/recipes.html'

class RecipeView(generic.ListView):
    model = Recipe
    template_name = 'blog/recipes.html' 