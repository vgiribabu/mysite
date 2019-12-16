from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Recipe
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, UserForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('recipes:index'))
        else:
            return HttpResponse("Invalid Credientials")
    return render(request, 'recipes/login.html')


def register(request):
    if request.method == 'POST':
        User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password'],
            email = request.POST['email'],
        )
        return HttpResponseRedirect(reverse('recipes:login'))
    return render(request, 'recipes/register.html')


def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('recipes:login'))


def index(request):
    re=Recipe.objects.all()
    context={'recipe':re}
    return render(request,'recipes/index.html',context)


def detail(request, recipe_id):
    check = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/detail.html', {'check': check})


@login_required(login_url='/recipes/create')
def create(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)

        # Recipe.objects.create(
            # creater=request.POST["creater"],
            # name = request.POST["name"],
            # ingredients = request.POST["ingredients"],
            # process = request.POST["process"],
            # date = timezone.now()

         # )
        f = form.save(commit=False)
        f.date = timezone.now()
        f.created_by = request.user
        f.save()
        if form.is_valid():
            return HttpResponseRedirect(reverse('recipes:index'))
    else:
        form = RecipeForm()
    return render(request, 'recipes/create.html', {'form': form})

def delete(request, del_id):
    a = get_object_or_404(Recipe, pk=del_id)
    a.delete()
    return HttpResponseRedirect(reverse('recipes:index'))


def users_view(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'recipes/users.html', context)