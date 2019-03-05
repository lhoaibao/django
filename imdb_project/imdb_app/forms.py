from django import forms
from django.forms import ModelMultipleChoiceField, CheckboxSelectMultiple
from .models import Movie, Actor
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms.fields import DateField


class PostMovieForm(forms.ModelForm):
    release_date = DateField(widget=forms.SelectDateWidget())
    # actors = ModelMultipleChoiceField(queryset=Actor.objects.all(), widget=CheckboxSelectMultiple())
    class Meta:
        model = Movie
        fields = '__all__'


class PostActorForm(forms.ModelForm):
    birthdate = DateField(widget=forms.SelectDateWidget())
    class Meta:
        model = Actor
        fields = '__all__'
