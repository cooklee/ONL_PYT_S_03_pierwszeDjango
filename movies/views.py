from django.http import HttpResponse
from django.shortcuts import render, redirect

filmy_list = ['Titanic', 'Avatar', 'New Hope', 'Noce i Dnie', 'Coś', 'The Crown']
aktorzy_list = ['Jaś Fasola', 'Carrie Fisher', 'Harrison Ford', 'Megan Fox', 'Cezary Pazura', 'janusz Gajos']
kina_list = ['Helios', 'Cinema City', 'Nowe Horyzonty']


# Create your views here.

def index(request):
    return render(request, 'base.html')

def wyszukaj(zapytanie, lista):
    ret_lst = []
    for movie in lista:
        if zapytanie in movie.lower():
            ret_lst.append(movie)
    return ret_lst


def filmy(request):
    zapytanie = request.GET.get('zapytanie', '').lower()
    ret_lst = wyszukaj(zapytanie, filmy_list)
    return render(request, 'list_view.html', {'object_list': ret_lst})


def aktorzy(request):
    zapytanie = request.GET.get('zapytanie', '').lower()
    ret_lst = wyszukaj(zapytanie, aktorzy_list)
    return render(request, 'list_view.html', {'object_list': ret_lst})


def kina(request):
    zapytanie = request.GET.get('zapytanie', '').lower()
    ret_lst = wyszukaj(zapytanie, kina_list)
    return render(request, 'list_view.html', {'object_list': ret_lst})

def dodaj_film(request):
    if request.method == 'GET':
        return render(request, 'dodaj_film.html')
    tytul = request.POST.get('title')
    filmy_list.append(tytul)
    return redirect("/filmy/")