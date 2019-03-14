from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
from .models import Movie, Actor, Award, Comment
from .forms import (PostMovieForm,
                    PostActorForm,
                    PostAwardForm,
                    SignUpForm,
                    PostCommentForm)
from django.contrib.contenttypes.models import ContentType


"-------------------------Sign Up-------------------------------------"


class SignUp(generic.CreateView):
    """ Create New User, if success go back to login page """
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


"-------------------------Movie-------------------------------------"


class MovieListView(generic.ListView):
    """ View list of movies """
    model = Movie
    # name to call in template
    context_object_name = 'movie_list'
    # template to show
    template_name = 'imdb_app/movie_page.html'
    # limit to 12 movies per page
    paginate_by = 12

    def get_context_data(self, **kwargs):
        """ Put form to kwargs to use in template """
        # get form to use in template
        kwargs['form'] = PostMovieForm()
        return super(MovieListView, self).get_context_data(**kwargs)


class MovieCreateView(generic.CreateView):
    """ Create movie and reverse back to movie page """
    # form to use to create
    form_class = PostMovieForm
    # if success reverse back to movie page
    success_url = reverse_lazy('imdb_app:movie')

    def form_valid(self, form):
        # get user that send the request
        form.instance.author = self.request.user
        return super(MovieCreateView, self).form_valid(form)


class MovieDetailView(generic.DetailView):
    """ Go to detail page of a specific movie with primary key """
    model = Movie

    def get_context_data(self, **kwargs):
        # get movie follow by it's primary key
        movie = Movie.objects.get(pk=self.kwargs['pk'])
        # get all of it's comments
        kwargs['comments'] = movie.comments.all()
        # get form to use in template
        kwargs['form'] = PostCommentForm()
        return super(MovieDetailView, self).get_context_data(**kwargs)


class MovieEditView(generic.UpdateView):
    """ Edit movie and reverse back to movie page """
    # form to use to edit
    form_class = PostMovieForm
    # get all movies objects
    queryset = Movie.objects.all()
    # template to use to show edit form
    template_name = 'imdb_app/edit.html'
    # if successfully edit reverse back to movie page
    success_url = reverse_lazy('imdb_app:movie')


class MovieDeleteView(generic.DeleteView):
    """ Delete movie by it's primary key and reverse back to movie page """
    # get all movies objects
    queryset = Movie.objects.all()
    # if delete success return to movie page
    success_url = reverse_lazy('imdb_app:movie')


"-------------------------Actor-------------------------------------"


class ActorListView(generic.ListView):
    """ View list of actors """
    model = Actor
    # name of model to use in template
    context_object_name = 'actor_list'
    # page to show all actors
    template_name = 'imdb_app/actor_page.html'
    # up to 12 actors per page
    paginate_by = 12

    def get_context_data(self, **kwargs):
        """ Put form to kwargs to use in template """
        kwargs['form'] = PostActorForm()
        return super(ActorListView, self).get_context_data(**kwargs)


class ActorCreateView(generic.CreateView):
    """ Create actor and reverse back to actor page """
    # form to use to create
    form_class = PostActorForm
    # if success reverse back to actor page
    success_url = reverse_lazy('imdb_app:actor')

    def form_valid(self, form):
        # get user that send the request and put it to form
        form.instance.author = self.request.user
        return super(ActorCreateView, self).form_valid(form)


class ActorDetailView(generic.DetailView):
    """ Go to detail page of a specific actor with primary key """
    model = Actor

    def get_context_data(self, **kwargs):
        # get actor follow by it's primary key
        actor = Actor.objects.get(pk=self.kwargs['pk'])
        # get all of it's comments
        kwargs['comments'] = actor.comments.all()
        # get form to use in template
        kwargs['form'] = PostCommentForm()
        return super(ActorDetailView, self).get_context_data(**kwargs)


class ActorEditView(generic.UpdateView):
    """ Edit actor and reverse back to actor page """
    # form to use to edit
    form_class = PostActorForm
    # get all actor objects
    queryset = Actor.objects.all()
    # template to use to show edit form
    template_name = 'imdb_app/edit.html'
    # if successfully edit reverse back to actor page
    success_url = reverse_lazy('imdb_app:actor')


class ActorDeleteView(generic.DeleteView):
    """ Delete actor by it's primary key and reverse back to actor page """
    # get all actor objects
    queryset = Actor.objects.all()
    # if delete success return to actor page
    success_url = reverse_lazy('imdb_app:actor')


"-------------------------Award-------------------------------------"


class AwardListView(generic.ListView):
    """ list all award data"""
    model = Award
    # name of model to use in template
    context_object_name = 'award_list'
    # temple to show awards
    template_name = 'imdb_app/award_page.html'

    def get_context_data(self, **kwargs):
        """ add varible to use data in template """
        # form to create award
        kwargs['form'] = PostAwardForm()
        # list of all movies
        kwargs['movie_list'] = Movie.objects.all()
        # list of all actors
        kwargs['actor_list'] = Actor.objects.all()
        # list all awarded movie
        kwargs['movie_award_list'] = Award.objects.filter(kind='Movie')
        # list all awarded actors
        kwargs['actor_award_list'] = Award.objects.filter(kind='Actor')
        return super(AwardListView, self).get_context_data(**kwargs)


class AwardMovieListView(generic.ListView):
    """ List all awarded movies view """
    model = Award
    # template to show
    template_name = 'imdb_app/award_list.html'

    def get_context_data(self, **kwargs):
        """ add variable to use data in template """
        # title of page
        kwargs['title'] = 'Movie Award'
        # form to create new award
        kwargs['form'] = PostAwardForm()
        # list of all awarded movies
        kwargs['data'] = Award.objects.filter(kind='Movie')
        return super(AwardMovieListView, self).get_context_data(**kwargs)


class AwardActorListView(generic.ListView):
    """ List all awarded actors view """
    model = Award
    # template to show
    template_name = 'imdb_app/award_list.html'

    def get_context_data(self, **kwargs):
        """ add variable to use data in template """
        # title of page
        kwargs['title'] = 'Actor Award'
        # form to create new award
        kwargs['form'] = PostAwardForm()
        # list of all awarded actors
        kwargs['data'] = Award.objects.filter(kind='Actor')
        return super(AwardActorListView, self).get_context_data(**kwargs)


class AwardCreateView(generic.CreateView):
    """ create new award view """
    form_class = PostAwardForm
    # if success redirect to award page
    success_url = reverse_lazy('imdb_app:award')

    def form_valid(self, form):
        """ get data for form """
        # get author
        form.instance.author = self.request.user
        # get object id
        form.instance.object_id = self.request._post['selected']
        # set variable to store kinh model
        model = self.request._post['kind'].lower()
        # get content type id (refference for model) for form
        form.instance.content_type_id = ContentType.objects.get(model=model).id
        return super(AwardCreateView, self).form_valid(form)


class AwardDetailView(generic.DetailView):
    """ show an award detail view"""
    model = Award

    def get_context_data(self, **kwargs):
        """ get variable to use in template """
        # get award by primary key
        award = Award.objects.get(pk=self.kwargs['pk'])
        # get all award comments
        kwargs['comments'] = award.comments.all()
        # form to create new comment
        kwargs['form'] = PostCommentForm()
        return super(AwardDetailView, self).get_context_data(**kwargs)


class AwardEditView(generic.UpdateView):
    """ edit award view """
    # form to use
    form_class = PostAwardForm
    # get all award objects
    queryset = Award.objects.all()
    # template for show
    template_name = 'imdb_app/award_edit.html'
    # if edit success redirect to award page
    success_url = reverse_lazy('imdb_app:award')

    def form_valid(self, form):
        """ fill form """
        # get author
        form.instance.author = self.request.user
        # get object id
        form.instance.object_id = self.request._post['selected']
        # set variable to store kinh model
        model = self.request._post['kind'].lower()
        # get content type id (refference for model) for form
        form.instance.content_type_id = ContentType.objects.get(model=model).id
        return super(AwardEditView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        """ get variable to use in template """
        # get all movie object
        kwargs['movie_list'] = Movie.objects.all()
        # get all actor object
        kwargs['actor_list'] = Actor.objects.all()
        return super(AwardEditView, self).get_context_data(**kwargs)


class AwardDeleteView(generic.DeleteView):
    """ delete award view """
    # get all award object
    queryset = Award.objects.all()
    # if delete success redirect to award page
    success_url = reverse_lazy('imdb_app:award')


"-------------------------Comment-------------------------------------"


class CommentCreateView(generic.CreateView):
    """ Create comment view """
    form_class = PostCommentForm

    def get_success_url(self):
        """ if success redirect to previous page """
        redirect_to = self.request._post['next']
        return redirect_to

    def form_valid(self, form):
        """ fill form """
        # get author
        form.instance.author = self.request.user
        # get object id
        form.instance.object_id = self.request.resolver_match.kwargs['pk']
        id = ContentType.objects.get(model=self.request._post['model']).id
        # get content type id (refference for model) for form
        form.instance.content_type_id = id
        return super(CommentCreateView, self).form_valid(form)


class CommentEditView(generic.UpdateView):
    """ edit comment view """
    # form to use
    form_class = PostCommentForm
    # get all comments objects
    queryset = Comment.objects.all()

    def get_success_url(self):
        """ if success redirect to previous page """
        redirect_to = self.request._post['next']
        return redirect_to


class CommentDeleteView(generic.DeleteView):
    """ delete comment view """
    queryset = Comment.objects.all()

    def get_success_url(self):
        """ if success redirect to previous page """
        redirect_to = self.request._post['next']
        return redirect_to
