from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
from .models import Movie, Actor, Award
from .forms import PostMovieForm, PostActorForm, PostAwardForm


"-------------------------Sign Up-------------------------------------"
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


"-------------------------Movie-------------------------------------"
class MovieView(generic.CreateView):
    form_class = PostMovieForm
    template_name = 'imdb_app/movie_page.html'
    success_url = reverse_lazy('imdb_app:movie')

    def get_context_data(self, **kwargs):
        kwargs['movie_list'] = Movie.objects.all()
        return super(MovieView, self).get_context_data(**kwargs)


class MovieDetailView(generic.DetailView):
    queryset = Movie.objects.all()

    def get_object(self):
        obj = super().get_object()
        return obj


"-------------------------Actor-------------------------------------"
class ActorView(generic.CreateView):
    form_class = PostActorForm
    template_name = 'imdb_app/actor_page.html'
    success_url = reverse_lazy('imdb_app:actor')

    def get_context_data(self, **kwargs):
        kwargs['actor_list'] = Actor.objects.all()
        return super(ActorView, self).get_context_data(**kwargs)


class ActorDetailView(generic.DetailView):
    queryset = Actor.objects.all()

    def get_object(self):
        obj = super().get_object()
        return obj


"-------------------------Award-------------------------------------"
class AwardView(generic.CreateView):
    template_name = 'imdb_app/award_page.html'
    form_class = PostAwardForm

    def get_queryset(self):
        return Award.objects.all()
