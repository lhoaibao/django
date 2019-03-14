from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


app_name = 'imdb_app'

urlpatterns = [
    # User
    path('signup/', views.SignUp.as_view(), name='signup'),

    # Movie
    path('movie/create', login_required(views.MovieCreateView.as_view()), name='movie_create'),
    path('movie/', login_required(views.MovieListView.as_view()), name='movie'),
    path('movie/<int:pk>', login_required(views.MovieDetailView.as_view()), name='movie_detail'),
    path('movie/<int:pk>/update', login_required(views.MovieEditView.as_view()), name='movie_edit'),
    path('movie/<int:pk>/delete', login_required(views.MovieDeleteView.as_view()), name='movie_delete'),

    # Actor
    path('actor/create', login_required(views.ActorCreateView.as_view()), name='actor_create'),
    path('actor/', login_required(views.ActorListView.as_view()), name='actor'),
    path('actor/<int:pk>', login_required(views.ActorDetailView.as_view()), name='actor_detail'),
    path('actor/<int:pk>/update', login_required(views.ActorEditView.as_view()), name='actor_edit'),
    path('actor/<int:pk>/delete', login_required(views.ActorDeleteView.as_view()), name='actor_delete'),

    # Award
    path('award/create', login_required(views.AwardCreateView.as_view()), name='award_create'),
    path('award/', login_required(views.AwardListView.as_view()), name='award'),
    path('award/<int:pk>', login_required(views.AwardDetailView.as_view()), name='award_detail'),
    path('award/<int:pk>/update', login_required(views.AwardEditView.as_view()), name='award_edit'),
    path('award/<int:pk>/delete', login_required(views.AwardDeleteView.as_view()), name='award_delete'),

    # Comment
    path('comment/<int:pk>/create', login_required(views.CommentCreateView.as_view()), name='comment_create'),
    path('comment/<int:pk>/update', login_required(views.CommentEditView.as_view()), name='comment_edit'),
    path('comment/<int:pk>/delete', login_required(views.CommentDeleteView.as_view()), name='comment_delete'),
]
