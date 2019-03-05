from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('movie/', views.MovieView.as_view(), name='movie'),
    path('actor/', views.ActorView.as_view(), name='actor'),
    path('award/', views.AwardView.as_view(), name='award'),
]
