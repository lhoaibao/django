from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
from .models import Movie, Actor, Award
from .forms import PostMovieForm, PostActorForm
from django.views.generic.edit import FormMixin
# Create your views here.

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class MovieView(generic.CreateView):
    form_class = PostMovieForm
    template_name = 'imdb_app/movie_page.html'
    success_url = reverse_lazy('movie')

    def get_context_data(self, **kwargs):
        kwargs['movie_list'] = Movie.objects.all()
        return super(MovieView, self).get_context_data(**kwargs)


class ActorView(generic.CreateView):
    form_class = PostActorForm
    template_name = 'imdb_app/actor_page.html'
    success_url = reverse_lazy('actor')

    def get_context_data(self, **kwargs):
        kwargs['actor_list'] = Actor.objects.all()
        return super(ActorView, self).get_context_data(**kwargs)


class AwardView(generic.ListView):
    template_name = 'imdb_app/award_page.html'

    def get_queryset(self):
        return Award.objects.all()
