from django import forms
from .models import Recipe, Comment


class RecipeForm(forms.ModelForm):
    """ Form to create a new recipe  """

    class Meta:
        model = Recipe
        fields = ['title', 'slug', 'ingredients', 'instructions', 'calories', 'image']
        

        ingredients = forms.CharField()
        instructions = forms.CharField()
        


        labels = {
            'title': 'Recipe Title',
            'slug': 'Description',
            'ingredients': 'Ingredients',
            'instructions': 'Instructions',
            'calories': 'Calories',
            'image': 'Image',
            'image_alt': 'Describe Image'
        }


class CommentForm(forms.ModelForm):
    """ Form to create a comment """
    class Meta:
        model = Comment
        fields = ('body',)

        labels = {
            'body': 'Comment'
        }