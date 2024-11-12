from django import forms
from .models import Recipe, Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class RecipeForm(forms.ModelForm):
    """ Form to create a new recipe  """
    class Meta:
        model = Recipe
        fields = ['title', 'description',
                  'ingredients', 'instructions', 'calories', 'image']

        widgets = {
            'ingredients': SummernoteWidget(),
            'instructions': SummernoteWidget()
        }
        labels = {
            'title': 'Recipe Title',
            'description': 'Description',
            'ingredients': 'Ingredients',
            'instructions': 'Instructions',
            'calories': 'Calories',
            'image': 'Image',
        }


class CommentForm(forms.ModelForm):
    """ Form to create a comment """
    class Meta:
        model = Comment
        fields = ('body',)

        labels = {
            'body': 'Comment'
        }
