from django import forms
from .models import Movie, Actor, Award, User, Comment
from django.forms.fields import DateField
from django.contrib.auth.forms import UserCreationForm
import datetime


class SignUpForm(UserCreationForm):
    """ Get field for user registeration """
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(
        max_length=254,
        help_text='Required. Inform a valid email address.'
    )

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'avatar'
        )


class PostMovieForm(forms.ModelForm):
    """ Create movie form excluding user in form """
    release_date = DateField(
        widget=forms.SelectDateWidget(
            years=range(datetime.date.today().year, 1800, -1))
        )

    class Meta:
        model = Movie
        exclude = ('author',)


class PostActorForm(forms.ModelForm):
    """ Create actor form excluding user in form """
    birthdate = DateField(
        widget=forms.SelectDateWidget(
            years=range(datetime.date.today().year, 1800, -1))
        )

    class Meta:
        model = Actor
        exclude = ('author',)


class PostAwardForm(forms.ModelForm):
    """ Create award form excluding user,
        content type and object id in form """
    date = DateField(
        widget=forms.SelectDateWidget(
            years=range(datetime.date.today().year, 1800, -1))
        )

    class Meta:
        model = Award
        exclude = ('author', 'content_type', 'object_id')


class PostCommentForm(forms.ModelForm):
    """ Create comment form """
    class Meta:
        model = Comment
        fields = ('comment_text',)
