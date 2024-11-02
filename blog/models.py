from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from djrichtextfield.models import RichTextField

class Recipe(models.Model):
    """
    A model to create recipes 
    """
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.title} | {self.author}"
    
    def get_absolute_url(self):
        return reverse("recipe", args=[str(self.id)])


    author = models.ForeignKey(User, related_name="recipe_owner", on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, null=False, unique=True)
    description = models.CharField(max_length=500, null=False, blank=False)
    ingredients = models.TextField(max_length=10000, null=False, blank=False)
    instructions = models.TextField(max_length=50000, null=False, blank=False)
    image = CloudinaryField('image', default='placeholder')
    image_alt = models.CharField(max_length=100, blank=False, null=False)
    calories = models.IntegerField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
        
    post = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    