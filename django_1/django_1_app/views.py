from django.shortcuts import render, redirect
from .models import Project, Task
from .forms import ProjectForm, TaskForm
from .forms import  RegistrationForm, LoginForm
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login


def project(request, **kwargs):
    project = Project.objects.get(id=kwargs['id'])
    # tasks = Task.objects.filter(project=project.id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            priority = form.cleaned_data['priority']
            deadline = form.cleaned_data['deadline']
            status = form.cleaned_data['status']
            task = Task(name=name, priority=priority, deadline=deadline, project=project, status=status)
            task.save()
            return redirect(f'/')
    else:
        form = TaskForm()
        tasks = Task.objects.filter(project=project)
        return render(request, 'project_page.html', {'project': project, 'tasks': tasks, 'form': form})


def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            project = Project(name=name)
            project.save()
            return redirect('/')
    else:
        form = ProjectForm()
        context = {'name': form}
        return render(request, 'project_create.html', context)

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
        return render(request, 'registration.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return redirect('/registration')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def home(request):
    names = ['Eldar', 'Denis', "Maria"]
    name = 'Geb'
    context = {'name': name, 'title': 'Home', 'names': names}
    return render(request, 'home.html', context)


# def about(request):
#    context = {'first_name': 'Eldar', 'last_name': 'Zanizdra', 'age': 14, 'city': 'Kyiv'}
#    return render(request, 'about_me.html', context)


#def page1(request):
#    if request.method == 'POST':
#        data = request.POST
#        name = data['name']
#        surname = data['surname']
#        age = data['age']
#        director = Directors(first_name=name, second_name=surname, age=age)
#        director.save()
#   return render(request, 'page1.html')


#def page2(request):
#   dirs = Directors.objects.all()
#    return render(request, 'page2.html', {'data': dirs})


#def page3(request):
#    if request.method == 'POST':
#        form = FilmForm1(request.POST)
#        if form.is_valid():
#            title = form.cleaned_data['title']
#            year = form.cleaned_data['year']
#            genre = form.cleaned_data['genre']
#            dir = Directors.objects.get(id=1)
#            film = Films(title=title, year=year, genre=genre, director=dir)
#            film.save()
#        return render(request, 'page3.html', {'form': form})
#    else:
#        form = FilmForm1()
#        return render(request, 'page3.html', {'form': form})


#def films(request):
#    film = Films.objects.all()
#    return render(request, 'films.html', {'films': film})
