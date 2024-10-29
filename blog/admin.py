from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Comment

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    list_display = (
        'title',
        'calories',
        # 'instructions',
        'ingredients',
        'image'
    )
    summernote_fields = ('instructions')


admin.site.register(Comment)






