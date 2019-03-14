from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
from .models import Movie, Actor, Award, Comment
from .forms import PostMovieForm, PostActorForm, PostAwardForm, SignUpForm, PostCommentForm
from django.contrib.contenttypes.models import ContentType


"-------------------------Sign Up-------------------------------------"


class SignUp(generic.CreateView):
    form_class = SignUpForm
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

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(MovieCreateView, self).form_valid(form)


class MovieDetailView(generic.DetailView):
    model = Movie

    def get_context_data(self, **kwargs):
        movie = Movie.objects.get(pk=self.kwargs['pk'])
        kwargs['comments'] = movie.comments.all()
        kwargs['form'] = PostCommentForm()
        return super(MovieDetailView, self).get_context_data(**kwargs)


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

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ActorCreateView, self).form_valid(form)


class ActorDetailView(generic.DetailView):
    model = Actor

    def get_context_data(self, **kwargs):
        actor = Actor.objects.get(pk=self.kwargs['pk'])
        kwargs['comments'] = actor.comments.all()
        kwargs['form'] = PostCommentForm()
        return super(ActorDetailView, self).get_context_data(**kwargs)


class ActorEditView(generic.UpdateView):
    form_class = PostActorForm
    queryset = Actor.objects.all()
    template_name = 'imdb_app/edit.html'
    success_url = reverse_lazy('imdb_app:actor')


class ActorDeleteView(generic.DeleteView):
    queryset = Actor.objects.all()
    success_url = reverse_lazy('imdb_app:actor')


"-------------------------Award-------------------------------------"


class AwardListView(generic.ListView):
    model = Award
    context_object_name = 'award_list'
    template_name = 'imdb_app/award_page.html'

    def get_context_data(self, **kwargs):
        kwargs['form'] = PostAwardForm()
        kwargs['movie_list'] = Movie.objects.all()
        kwargs['actor_list'] = Actor.objects.all()
        kwargs['movie_award_list'] = Award.objects.filter(kind='Movie')
        kwargs['actor_award_list'] = Award.objects.filter(kind='Actor')
        return super(AwardListView, self).get_context_data(**kwargs)


class AwardMovieListView(generic.ListView):
    model = Award
    template_name = 'imdb_app/award_list.html'

    def get_context_data(self, **kwargs):
        kwargs['title'] = 'Movie Award'
        kwargs['form'] = PostAwardForm()
        kwargs['data'] = Award.objects.filter(kind='Movie')
        return super(AwardMovieListView, self).get_context_data(**kwargs)


class AwardActorListView(generic.ListView):
    model = Award
    template_name = 'imdb_app/award_list.html'

    def get_context_data(self, **kwargs):
        kwargs['title'] = 'Actor Award'
        kwargs['form'] = PostAwardForm()
        kwargs['data'] = Award.objects.filter(kind='Actor')
        return super(AwardActorListView, self).get_context_data(**kwargs)


class AwardCreateView(generic.CreateView):
    form_class = PostAwardForm
    success_url = reverse_lazy('imdb_app:award')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.object_id = self.request._post['selected']
        model = self.request._post['kind'].lower()
        form.instance.content_type_id = ContentType.objects.get(model=model).id
        return super(AwardCreateView, self).form_valid(form)


class AwardDetailView(generic.DetailView):
    model = Award

    def get_context_data(self, **kwargs):
        award = Award.objects.get(pk=self.kwargs['pk'])
        kwargs['comments'] = award.comments.all()
        kwargs['form'] = PostCommentForm()
        return super(AwardDetailView, self).get_context_data(**kwargs)


class AwardEditView(generic.UpdateView):
    form_class = PostAwardForm
    queryset = Award.objects.all()
    template_name = 'imdb_app/award_edit.html'
    success_url = reverse_lazy('imdb_app:award')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.object_id = self.request._post['selected']
        model = self.request._post['kind'].lower()
        form.instance.content_type_id = ContentType.objects.get(model=model).id
        return super(AwardEditView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['movie_list'] = Movie.objects.all()
        kwargs['actor_list'] = Actor.objects.all()
        return super(AwardEditView, self).get_context_data(**kwargs)


class AwardDeleteView(generic.DeleteView):
    queryset = Award.objects.all()
    success_url = reverse_lazy('imdb_app:award')


class CommentCreateView(generic.CreateView):
    form_class = PostCommentForm

    def get_success_url(self):
        redirect_to=self.request._post['next']
        return redirect_to

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.object_id = self.request.resolver_match.kwargs['pk']
        form.instance.content_type_id = ContentType.objects.get(model=self.request._post['model']).id
        return super(CommentCreateView, self).form_valid(form)


class CommentEditView(generic.UpdateView):
    form_class = PostCommentForm
    queryset = Comment.objects.all()

    def get_success_url(self):
        redirect_to = self.request._post['next']
        return redirect_to


class CommentDeleteView(generic.DeleteView):
    queryset = Comment.objects.all()

    def get_success_url(self):
        redirect_to=self.request._post['next']
        return redirect_to
