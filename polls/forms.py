from django.forms import ModelForm
from .models import Recipe
from django.contrib.auth.models import User


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields=['name', 'ingredients', 'process','image']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']




