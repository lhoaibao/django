from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


app_name = 'imdb_app'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('movie/', login_required(views.MovieListView.as_view()), name='movie'),
    path('actor/', login_required(views.ActorListView.as_view()), name='actor'),
    path('award/', login_required(views.AwardCreateView.as_view()), name='award'),
    path('movie/<int:pk>', login_required(views.MovieDetailView.as_view()), name='movie_detail'),
    path('actor/<int:pk>', login_required(views.ActorDetailView.as_view()), name='actor_detail'),
    path('movie/create', login_required(views.MovieCreateView.as_view()), name='movie_create'),
    path('actor/create', login_required(views.ActorCreateView.as_view()), name='actor_create'),
    path('movie/<int:pk>/delete', login_required(views.MovieDeleteView.as_view()), name='movie_delete'),
    path('actor/<int:pk>/delete', login_required(views.ActorDeleteView.as_view()), name='actor_delete'),
    path('movie/<int:pk>/update', login_required(views.MovieEditView.as_view()), name='movie_edit'),
    path('actor/<int:pk>/update', login_required(views.ActorEditView.as_view()), name='actor_edit'),
]
