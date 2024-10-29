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
            return f"{self.title} | {self.user}"

    author = models.ForeignKey(User, related_name="recipe_owner", on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    ingredients = models.TextField()
    instructions = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    image_alt = models.CharField(max_length=100, blank=False, null=False)
    calories = models.IntegerField()
    created_on = models.DateTimeField(auto_now=True)


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

    