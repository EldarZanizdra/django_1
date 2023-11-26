from django import forms
from .models import Project, Task
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegistrationForm(UserCreationForm):
    username = forms.CharField(help_text="")
    email = forms.EmailField(help_text="")
    password1 = forms.CharField(help_text="", widget=forms.PasswordInput)
    password2 = forms.CharField(help_text="", widget=forms.PasswordInput)


class LoginForm(AuthenticationForm):
    username = forms.CharField(help_text="")
    password = forms.CharField(help_text="", widget=forms.PasswordInput)


#class FilmForm(forms.Form):
#    title = forms.CharField()
#    year = forms.DateField()
#   genre = forms.CharField()


#class FilmForm1(forms.ModelForm):
#    class Meta:
#        model = Films
#        fields = ['title', 'year', 'genre']


#class BookForm(forms.Form):
#    title = forms.CharField()
#    year = forms.DateField()
#    author = forms.CharField()


#class BookForm1(forms.ModelForm):
#   class Meta:
#        model = Films
#        fields = ['title', 'year', 'author']
#        widgets = {'year': forms.DateInput(attrs={'class': 'input1', 'id': 'id1', 'required': False})}


class ProjectForm(forms.ModelForm):
    class Meta():
        model = Project
        fields = ['name']


class TaskForm(forms.ModelForm):
    class Meta():
        model = Task
        fields = ['name', 'status', 'deadline', 'priority']
