import django_filters
from .models import Movie


class MovieFilter(django_filters.FilterSet):
    movie_time = django_filters.RangeFilter()
    year = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Movie
        fields = [
            'movie_time',
            'year',
            'country',
            'genre',
            'status_movie',
        ]


