from django.views.generic import TemplateView, ListView, CreateView
from .models import Recipe, Comment
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.views.generic.edit import FormMixin 
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipeForm, CommentForm
from django.http import HttpResponse, HttpResponseRedirect
from django import forms



# Create your views here.

class Index(TemplateView):
    template_name = 'blog/index.html'


class RecipeView(ListView, LoginRequiredMixin):
    # model = Recipe
    queryset = Recipe.objects.all()
    template_name = 'blog/recipes.html' 
    context_object_name = 'recipes'
    paginate_by = 6



def recipe_detail(request, slug):
    queryset = Recipe.objects.filter(approved=True)
    post = get_object_or_404(queryset, slug=slug)

    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid:
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            # messages.add_message(
            #     request, messages.SUCCESS,
            #     'Comment submitted and awaiting approval'
            # )
    comment_form = CommentForm()
    return render(
        request,
        'blog/recipe_detail.html',
        {
        'post':post,
        'comments':comments,
        'comment_form': comment_form,
        'comment_count':comment_count
        },
    )

      

    
        


class AddRecipe(LoginRequiredMixin, CreateView):
    template_name = 'blog/add_recipe.html'
    model = Recipe
    form_class = RecipeForm
    success_url = '/recipes/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddRecipe, self).form_valid(form)



        

