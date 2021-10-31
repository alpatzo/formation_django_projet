from django.http import request
from django.shortcuts import render, redirect

from main.decorators import allowed_users, unauthenticated_user
from .models import *
from .form import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model

# Create your views here.


def home(request):
    appel_offre = Appel_Offre.objects.all()
    context = {'appel_offre': appel_offre}
    return render(request, 'home.html', context)


@allowed_users(['admin'])
def add(request):
    form = AppelOffreForm()
    if request.method == 'POST':
        form = AppelOffreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'add.html', context)


@allowed_users(['admin'])
def update(request, pk):
    updateOffre = Appel_Offre.objects.get(id=pk)
    form = AppelOffreForm(instance=updateOffre)
    if request.method == 'POST':
        form = AppelOffreForm(request.POST, instance=updateOffre)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'add.html', context)


@allowed_users(['admin'])
def supp(request, pk):
    suppOffre = Appel_Offre.objects.get(id=pk)
    if request.method == 'POST':
        suppOffre.delete()
        return redirect('home')
    context = {'suppOffre': suppOffre}
    return render(request, 'supp.html', context)


@login_required(login_url='login')
def add_postule(request, pk):
    #titre = Appel_Offre.objects.filter(id=pk).values('titre')
    t = Appel_Offre.objects.get(id=pk)
    b = t.titre
    id = t.id
    print(b)
    print(id)
    #a = titre[0].get('titre')
    init = {
        "titre": id,
        "detail": "",
        "budget": 0,
        "duree": "",
        "nom_responsable": ""
    }
    form = PosteForm(initial=init)
    if request.method == 'POST':
        form = PosteForm(request.POST, initial=init)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form, 'titre': b}
    return render(request, 'postuler.html', context)


@allowed_users(['gestionaire', 'admin'])
def aff_postule(request):
    poste = postulation.objects.all()
    context = {'poste': poste}
    return render(request, 'affiche_poste.html', context)


@allowed_users(['gestionaire', 'admin'])
def supp_postule(request, pk):
    suppPoste = postulation.objects.get(id=pk)
    if request.method == 'POST':
        suppPoste.delete()
        return redirect('home')
    context = {'suppPoste': suppPoste}
    return render(request, 'supp.html', context)


@allowed_users(['gestionaire', 'admin'])
def update_postule(request, pk):
    updatePoste = postulation.objects.get(id=pk)
    form = PosteForm(instance=updatePoste)
    if request.method == 'POST':
        form = PosteForm(request.POST, instance=updatePoste)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'postuler.html', context)


@unauthenticated_user
def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'registre.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password is inncorect')
    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@allowed_users(allowed_roles=['user', 'gestionaire', 'admin'])
def profile(request):
    context = {}
    return render(request, 'profile.html')


'''affichier users coté admin'''


def aff_user(request):
    User = get_user_model()
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'aff_user.html', context)


def aff_un_user(request, pk):
    User = get_user_model()
    users = User.objects.values()
    context = {'users': users}
    return render(request, 'aff_user.html', context)
