from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Recipe


class RecipeForm(forms.ModelForm):
    """ Form to create a new recipe  """

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions', 'calories', 'image', 'image_alt']

        ingredients = forms.CharField(widget=RichTextWidget())
        instructions = forms.CharField(widget=RichTextWidget())

        widget = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }


        labels = {
            'title': 'Recipe Title',
            'description': 'Description',
            'ingredients': 'Ingredients',
            'instructions': 'Instructions',
            'calories': 'Calories',
            'image': 'Image',
            'image_alt': 'Describe Image'
        }