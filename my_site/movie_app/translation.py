from .models import Category, Country, Genre, Actor, Director, Movie, MovieLanguages
from modeltranslation.translator import TranslationOptions, register

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)


@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('genre_name',)


@register(Director)
class DirectorTranslationOptions(TranslationOptions):
    fields = ('director_name', 'bio')


@register(Actor)
class ActorTranslationOptions(TranslationOptions):
    fields = ('actor_name', 'bio')


@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('movie_name', 'slogan', 'description')


@register(MovieLanguages)
class MovieLanguagesTranslationOptions(TranslationOptions):
    fields = ('language',)