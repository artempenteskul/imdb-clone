from django.contrib import admin

from .models import Movie, MovieImage, Person, Role, Vote


admin.site.register(Movie)
admin.site.register(Person)
admin.site.register(MovieImage)
admin.site.register(Role)
admin.site.register(Vote)
