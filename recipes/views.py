from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.

def recipe_list(request):
  recipes = Recipe.objects.all()

  context = {
    'recipes':recipes
  }

  return render(request, 'recipe_list.html',context) 

def recipe_form(request):
  
  form=RecipeForm()

  if request.method == "POST":
    print("form submitted")
    form = RecipeForm(request.POST,request.FILES)

    if form.is_valid():
      messages.error(request, "Recipe already exists!")
      form.save()
      messages.success(request, "Recipe added successfully!")
      return redirect('recipe_list')

  context = {
    'form':form
  }
    
  return render(request, 'recipe_form.html',context)