from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Comment


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    list_display = (
        'title',
        'slug',
        'status',
        'created_on',
        'approved',
    )
    prepopulated_fields = {"slug": ("title", )}
    search_fields = ['title']
    list_filter = ['status', 'created_on']
    summernote_fields = ('instructions', 'ingredients')


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_display = (
        'author',
        'body',
        'recipe',
        'created_on',
        'approved',
    )
    list_filter = ['approved','created_on']

