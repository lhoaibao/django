from django.contrib import admin
from .models import Movie, Actor, Category, Comment


admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Category)
admin.site.register(Comment)
