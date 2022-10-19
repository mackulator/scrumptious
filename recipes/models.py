from django.db import models

# Create your models here.
class Recipe(models.Model):
  title = models.CharField(max_length=200)
  # author = models.ForeignKey(
  #   related_name='recipes',
  #   on_delete=models.CASCADE,
  #   null=True,
  # )
  picture = models.URLField(null=True, blank=True)
  description = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
