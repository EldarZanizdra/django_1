from django.shortcuts import render
from django.http import HttpResponse
from .models import Directors, Films
from .forms import FilmForm1


def home(request):
    names = ['Eldar', 'Denis', "Maria"]
    name = 'Geb'
    context = {'name': name, 'title': 'Home', 'names': names}
    return render(request, 'home.html', context)


def about(request):
    context = {'first_name': 'Eldar', 'last_name': 'Zanizdra', 'age': 14, 'city': 'Kyiv'}
    return render(request, 'about_me.html', context)


def page1(request):
    if request.method == 'POST':
        data = request.POST
        name = data['name']
        surname = data['surname']
        age = data['age']
        director = Directors(first_name=name, second_name=surname, age=age)
        director.save()
    return render(request, 'page1.html')


def page2(request):
    dirs = Directors.objects.all()
    return render(request, 'page2.html', {'data': dirs})


def page3(request):
    if request.method == 'POST':
        form = FilmForm1(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            year = form.cleaned_data['year']
            genre = form.cleaned_data['genre']
            dir = Directors.objects.get(id=1)
            film = Films(title=title, year=year, genre=genre, director=dir)
            film.save()
        return render(request, 'page3.html', {'form': form})
    else:
        form = FilmForm1()
        return render(request, 'page3.html', {'form': form})


def films(request):
    film = Films.objects.all()
    return render(request, 'films.html', {'films': film})
