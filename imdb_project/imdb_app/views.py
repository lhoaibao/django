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


class MovieListView(generic.ListView):
    model = Movie
    context_object_name = 'movie_list'
    template_name = 'imdb_app/movie_page.html'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        kwargs['form'] = PostMovieForm()
        return super(MovieListView, self).get_context_data(**kwargs)


class MovieCreateView(generic.CreateView):
    form_class = PostMovieForm
    success_url = reverse_lazy('imdb_app:movie')


class MovieDetailView(generic.DetailView):
    model = Movie


class MovieEditView(generic.UpdateView):
    form_class = PostMovieForm
    queryset = Movie.objects.all()
    template_name = 'imdb_app/edit.html'
    success_url = reverse_lazy('imdb_app:movie')


class MovieDeleteView(generic.DeleteView):
    queryset = Movie.objects.all()
    template_name = 'imdb_app/delete.html'
    success_url = reverse_lazy('imdb_app:movie')


"-------------------------Actor-------------------------------------"


class ActorListView(generic.ListView):
    model = Actor
    context_object_name = 'actor_list'
    template_name = 'imdb_app/actor_page.html'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        kwargs['form'] = PostActorForm()
        return super(ActorListView, self).get_context_data(**kwargs)


class ActorCreateView(generic.CreateView):
    form_class = PostActorForm
    success_url = reverse_lazy('imdb_app:actor')


class ActorDetailView(generic.DetailView):
    model = Actor


class ActorEditView(generic.UpdateView):
    form_class = PostActorForm
    queryset = Actor.objects.all()
    template_name = 'imdb_app/edit.html'
    success_url = reverse_lazy('imdb_app:actor')


class ActorDeleteView(generic.DeleteView):
    queryset = Actor.objects.all()
    template_name = 'imdb_app/delete.html'
    success_url = reverse_lazy('imdb_app:actor')


"-------------------------Award-------------------------------------"


class AwardCreateView(generic.CreateView):
    template_name = 'imdb_app/award_page.html'
    form_class = PostAwardForm

    def get_queryset(self):
        return Award.objects.all()
