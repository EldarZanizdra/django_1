from django import forms
from .models import Films


class FilmForm(forms.Form):
    title = forms.CharField()
    year = forms.DateField()
    genre = forms.CharField()


class FilmForm1(forms.ModelForm):
    class Meta:
        model = Films
        fields = ['title', 'year', 'genre']
