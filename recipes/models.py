from django.db import models

# Create your models here.

DIFFICULTY_CHOICES = [
  ('Easy', 'Easy'),
  ('Medium','Medium'),
  ('Hard','Hard')
]

class Recipe(models.Model):
  name =  models.CharField(max_length=100,unique=True)
  ingredients = models.TextField()
  cooking_time = models.PositiveIntegerField()
  difficulty_level =  models.CharField(max_length=10,choices=DIFFICULTY_CHOICES) 
  instructions =  models.TextField()
  image =  models.ImageField(
    upload_to='recipes/',
    blank=True,
    null=True
  )


  def __str__(self):
    return self.name