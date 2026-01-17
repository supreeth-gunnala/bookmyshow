from django.contrib import admin
from .models import Movie, Genre, Language


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'price')
    list_filter = ('genre', 'language')
    search_fields = ('title',)


admin.site.register(Genre)
admin.site.register(Language)
