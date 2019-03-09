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
class MovieCreateView(generic.CreateView):
    form_class = PostMovieForm
    template_name = 'imdb_app/movie_page.html'
    success_url = reverse_lazy('imdb_app:movie')

    def get_context_data(self, **kwargs):
        kwargs['movie_list'] = Movie.objects.all()
        return super(MovieCreateView, self).get_context_data(**kwargs)


class MovieDeleteView(generic.DeleteView):
    queryset = Movie.objects.all()
    template_name = 'imdb_app/delete.html'
    success_url = reverse_lazy('imdb_app:movie')


class MovieEditView(generic.UpdateView):
    form_class = PostMovieForm
    queryset = Movie.objects.all()
    template_name = 'imdb_app/edit.html'
    success_url = reverse_lazy('imdb_app:movie')


class MovieDetailView(generic.DetailView):
    model = Movie


"-------------------------Actor-------------------------------------"
class ActorCreateView(generic.CreateView):
    form_class = PostActorForm
    template_name = 'imdb_app/actor_page.html'
    success_url = reverse_lazy('imdb_app:actor')

    def get_context_data(self, **kwargs):
        kwargs['actor_list'] = Actor.objects.all()
        return super(ActorCreateView, self).get_context_data(**kwargs)


class ActorDeleteView(generic.DeleteView):
    queryset = Actor.objects.all()
    template_name = 'imdb_app/delete.html'
    success_url = reverse_lazy('imdb_app:actor')


class ActorEditView(generic.UpdateView):
    form_class = PostActorForm
    queryset = Actor.objects.all()
    template_name = 'imdb_app/edit.html'
    success_url = reverse_lazy('imdb_app:actor')


class ActorDetailView(generic.DetailView):
    model = Actor


"-------------------------Award-------------------------------------"
class AwardCreateView(generic.CreateView):
    template_name = 'imdb_app/award_page.html'
    form_class = PostAwardForm

    def get_queryset(self):
        return Award.objects.all()
