from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .models import Project, Task, Users
from django.urls import reverse_lazy
from .forms import ProjectForm, TaskForm
# from .forms import  RegistrationForm, LoginForm
from .forms import RegistrationForm, LoginForm
# from django.contrib.auth import authenticate, login
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


class TestPage(TemplateView):
    template_name = 'test.html'

    def post(self, request):
        data = request.POST
        return JsonResponse({'resp': data['text']})


class ProjectView(TemplateView):
    template_name = 'project_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = Project.objects.get(id=self.kwargs['id'])
        tasks = Task.objects.filter(project=project)
        context['project'] = project
        context['tasks'] = tasks
        context['form'] = TaskForm()
        return context

    def get_success_url(self, **kwargs):
        return f"/project_page/{self.kwargs["id"]}"

    def post(self, request, **kwargs):
        data = request.POST
        task = Task(name=data['name'], status=True if data['status'] == 'on' else False, deadline=data['deadline'], priority=data['priority'], project=Project.objects.get(id=self.kwargs['id']))
        task.save()
        resp = render_to_string('task.html', {'i': task})
        return JsonResponse(resp, safe=False)


# def project(request, **kwargs):
#    project = Project.objects.get(id=kwargs['id'])
#    if request.method == 'POST':
#        form = TaskForm(request.POST)
#        if form.is_valid():
#            name = form.cleaned_data['name']
#            priority = form.cleaned_data['priority']
#            deadline = form.cleaned_data['deadline']
#            status = form.cleaned_data['status']
#            task = Task(name=name, priority=priority, deadline=deadline, project=project, status=status)
#           task.save()
#            return redirect(f'/')
#    else:
#        form = TaskForm()
#        tasks = Task.objects.filter(project=project)
#        return render(request, 'project_page.html', {'project': project, 'tasks': tasks, 'form': form})


def project_edit(request, **kwargs):
    p = Project.objects.get(id=kwargs['id'])
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            p.name = name
            p.save()
            return redirect(f'/')
    else:
        form = ProjectForm(initial={'name': p.name})
        context = {'form': form}
        return render(request, "project_edit.html", context)


class RegistrationView(CreateView):
    template_name = 'registration.html'
    model = Users
    form_class = RegistrationForm
    success_url = reverse_lazy('/')

    def get_success_url(self, **kwargs):
        self.object.username
        response = HttpResponse()
        response.set_cookie('name', 'Bob')
        self.request.COOKIES['username']
        return '/'


class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = self.request.user
        context['user_profile'] = user_profile
        return context


# def registration(request):
#   if request.method == 'POST':
#        form = RegistrationForm(request.POST)
#        if form.is_valid():
#            username = form.cleaned_data['username']
#            email = form.cleaned_data['email']
#            password = form.cleaned_data['password1']
#            user = User.objects.create_user(username=username, email=email, password=password)
#            user.save()
#            login(request, user)
#            return redirect('/')
#    else:
#        form = RegistrationForm()
#        return render(request, 'registration.html', {'form': form})


class LoginPage(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    redirect_authenticated_user = True


class LogoutPage(LogoutView):
    pass


# def login_page(request):
#    if request.method == 'POST':
#        form = LoginForm(request.POST)
#        if form.is_valid():
#            username = form.cleaned_data['username']
#           password = form.cleaned_data['password']
#            user = authenticate(request, username=username, password=password)
#            if user is not None:
#                login(request, user)
#                return redirect('/')
#            else:
#                return redirect('/registration')
#    else:
#        form = LoginForm()
#        return render(request, 'login.html', {'form': form})


class HomeView(ListView):
    model = Project
    paginate_by = 2
    template_name = 'home.html'
    context_object_name = 'projects'


# def home(request):
    # user = request.user
    # projects = Project.objects.all()
    # context = {'username': user, 'projects': projects}
    # return render(request, 'home.html', context)


# def about(request):
#    context = {'first_name': 'Eldar', 'last_name': 'Zanizdra', 'age': 14, 'city': 'Kyiv'}
#    return render(request, 'about_me.html', context)


# def page1(request):
#    if request.method == 'POST':
#        data = request.POST
#        name = data['name']
#        surname = data['surname']
#        age = data['age']
#        director = Directors(first_name=name, second_name=surname, age=age)
#        director.save()
#   return render(request, 'page1.html')


# def page2(request):
#   dirs = Directors.objects.all()
#    return render(request, 'page2.html', {'data': dirs})


# def page3(request):
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


# def films(request):
#    film = Films.objects.all()
#    return render(request, 'films.html', {'films': film})
