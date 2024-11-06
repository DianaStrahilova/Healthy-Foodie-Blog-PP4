from django.views.generic import TemplateView, ListView, CreateView
from .models import Recipe, Comment
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.views.generic.edit import FormMixin 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import RecipeForm, CommentForm
from django.http import HttpResponse, HttpResponseRedirect
from django import forms




# Create your views here.

class Index(TemplateView):
    template_name = 'blog/index.html'


class RecipeView(ListView):
    # model = Recipe
    queryset = Recipe.objects.filter(status=1)
    template_name = 'blog/recipes.html' 
    context_object_name = 'recipes'
    paginate_by = 6



def recipe_detail(request, slug):
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)

    comments = recipe.comments.all().order_by("-created_on")
    comment_count = recipe.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid:
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
    comment_form = CommentForm()
    return render(
        request,
        'blog/recipe_detail.html',
        {
        'recipe':recipe,
        'comments':comments,
        'comment_form': comment_form,
        'comment_count':comment_count,
        },
    )

def recipe_edit(request, slug):
    if request.method == "POST":
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        recipe_form = RecipeForm(data=request.POST, instance=recipe)

        if recipe_form.is_valid() and recipe.author == request.user:
            recipe = recipe_form.save(commit=False)
            recipe.approved = False
            recipe.save()
    return HttpResponseRedirect(reverse('add_recipe', args=[slug]))




def comment_edit(request, slug, comment_id):
    if request.method == "POST":

        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.approved = False
            comment.save()
    return HttpResponseRedirect(reverse('recipe', args=[slug]))



def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()

    return HttpResponseRedirect(reverse('recipe', args=[slug]))












class AddRecipe(LoginRequiredMixin, CreateView):
    template_name = 'blog/add_recipe.html'
    model = Recipe
    form_class = RecipeForm
    success_url = '/recipes/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddRecipe, self).form_valid(form)



        

