from .models import Recipe, Comment
from .forms import RecipeForm, CommentForm
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django import forms


# Home view
class Index(TemplateView):
    template_name = 'blog/index.html'


# Recipe list view
class RecipeView(ListView):
    queryset = Recipe.objects.filter(status=1)
    template_name = 'blog/recipes.html'
    context_object_name = 'recipes'
    paginate_by = 6


# Recipe detail view
def recipe_detail(request, slug):
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)

    comments = recipe.comments.all().order_by("-created_on")
    comment_count = recipe.comments.filter(approved=True).count()
    # Leave a comment
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
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
           'recipe': recipe,
           'comments': comments,
           'comment_form': comment_form,
           'comment_count': comment_count,
        },
    )


# Edit comment
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
            messages.add_message(request, messages.SUCCESS,
                                 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('recipe', args=[slug]))


# Delete comment
def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')

    return HttpResponseRedirect(reverse('recipe', args=[slug]))


# Add recipe
class AddRecipe(LoginRequiredMixin, CreateView):
    template_name = 'blog/add_recipe.html'
    model = Recipe
    form_class = RecipeForm
    success_url = '/recipes/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddRecipe, self).form_valid(form)


# Edit recipe
class EditRecipe(UpdateView):
    """ Edit a recipe """
    template_name = 'blog/edit_recipe.html'
    model = Recipe
    form_class = RecipeForm
    success_url = '/recipes/'
    

# Delete recipe
class DeleteRecipe(DeleteView):
    template_name = 'blog/delete_recipe.html'
    model = Recipe
    success_url = '/recipes/'

