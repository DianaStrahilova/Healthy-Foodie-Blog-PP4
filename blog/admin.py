from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'calories',
        'instructions',
        'ingredients',
        'image'
    )






