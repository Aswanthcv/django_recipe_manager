from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name ='recipe_list'),
    path('recipe_form',views.recipe_form, name ='recipe_form')

]