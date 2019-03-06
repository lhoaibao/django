from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


app_name = 'imdb_app'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('movie/', login_required(views.MovieView.as_view()), name='movie'),
    path('actor/', login_required(views.ActorView.as_view()), name='actor'),
    path('award/', login_required(views.AwardView.as_view()), name='award'),
    path('movie/<int:pk>', login_required(views.MovieDetailView.as_view()), name='movie_detail'),
    path('actor/<int:pk>', login_required(views.ActorDetailView.as_view()), name='actor_detail')
]
