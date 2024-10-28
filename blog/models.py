from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField




class Recipe(models.Model):
    """
    A model to create recipes 
    """
    class Meta:
        ordering = ['-created_on']

        def __str__(self):
            return str(self.title)

    user = models.ForeignKey(User, related_name="recipe_owner", on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    ingredients = models.TextField()
    instructions = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    image_alt = models.CharField(max_length=100, blank=False, null=False)
    calories = models.IntegerField()
    created_on = models.DateTimeField(auto_now=True)

    