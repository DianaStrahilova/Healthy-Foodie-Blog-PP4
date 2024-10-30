from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Comment

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    list_display = (
        'title',
        'slug',
        'calories',
        'ingredients',
        "image",
        'created_on'
    )
    search_fields = ['title']
    list_filter = ('created_on', )
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ('instructions')
   


admin.site.register(Comment)






