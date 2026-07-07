from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name ='recipe_list'),
    path('recipe_form',views.recipe_form, name ='recipe_form'),
    path('recipe_details/<int:id>/',views.recipe_details, name ='recipe_details'),
    path('edit_recipe/<int:id>',views.edit_recipe, name ='edit_recipe'),
    path('delete_recipe/<int:id>',views.delete_recipe, name ='delete_recipe'),
    path('confirm_delete/<int:id>',views.confirm_delete, name = 'confirm_delete'),
]