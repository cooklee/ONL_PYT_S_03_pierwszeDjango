from django.http import HttpResponse
from django.shortcuts import render, redirect
from movies.models import Person, Movie

filmy_list = ['Titanic', 'Avatar', 'New Hope', 'Noce i Dnie', 'Coś', 'The Crown']
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
    ret_lst = Movie.objects.all()
    return render(request, 'list_view.html', {'object_list': ret_lst})


def aktorzy(request):
    # zapytanie = request.GET.get('zapytanie', '').lower()
    ret_lst = Person.objects.all()
    return render(request, 'list_view.html', {'object_list': ret_lst})


def detail_actor_view(request, id):
    aktor = Person.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'actor_detail.html', {'object': aktor})
    imie = request.POST.get('imie')
    nazwisko = request.POST.get('nazwisko')
    description = request.POST.get('description')
    aktor.first_name = imie
    aktor.last_name = nazwisko
    aktor.description = description
    aktor.save()
    return render(request, 'actor_detail.html', {'object': aktor})

def dodaj_aktora(request):
    if request.method == 'GET':
        return render(request, 'add_actor.html')
    imie = request.POST.get('imie')
    nazwisko = request.POST.get('nazwisko')
    p = Person(first_name=imie, last_name=nazwisko)
    p.save()
    return render(request, 'add_actor.html')


def kina(request):
    zapytanie = request.GET.get('zapytanie', '').lower()
    ret_lst = wyszukaj(zapytanie, kina_list)
    return render(request, 'list_view.html', {'object_list': ret_lst})

def dodaj_film(request):
    if request.method == 'GET':
        return render(request, 'dodaj_film.html')
    tytul = request.POST.get('title')
    year = request.POST.get('year')
    m = Movie(title=tytul, year=year)
    m.save()
    return redirect("/filmy/")


def delete_person_view(request, id):
    p = Person.objects.get(pk=id)
    if request.method == 'GET':
        return render(request, 'del_p.html', {'person':p})
    ans = request.POST.get('conf')
    if ans == 'tak':
        p.delete()
    return redirect('/aktorzy/')



