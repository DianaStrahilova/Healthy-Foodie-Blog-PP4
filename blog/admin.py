from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Comment

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    list_display = (
        'title',
        'calories',
        'ingredients',
        "image",
        'created_on'
    )
    search_fields = ['title']
    list_filter = ('created_on', )
    summernote_fields = ('instructions', 'ingredients')
   


admin.site.register(Comment)






