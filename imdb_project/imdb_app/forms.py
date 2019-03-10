from django import forms
from django.forms import ModelMultipleChoiceField, CheckboxSelectMultiple
from .models import Movie, Actor, Award
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms.fields import DateField
import datetime


class PostMovieForm(forms.ModelForm):
    release_date = DateField(widget=forms.SelectDateWidget(years=range(datetime.date.today().year, 1800, -1)))

    class Meta:
        model = Movie
        fields = '__all__'


class PostActorForm(forms.ModelForm):
    birthdate = DateField(widget=forms.SelectDateWidget(years=range(datetime.date.today().year, 1800, -1)))
    class Meta:
        model = Actor
        fields = '__all__'


class PostAwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = '__all__'
