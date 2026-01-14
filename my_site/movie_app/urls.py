from rest_framework import routers
from .views import *
from django.urls import path, include


router = routers.DefaultRouter()

router.register(r'user', UserProfileViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'country', CountryViewSet)
router.register(r'director', DirectorViewSet)
router.register(r'actor', ActorViewSet)
router.register(r'genre', GenreViewSet)
router.register(r'movie_language', MovieLanguagesViewSet)
router.register(r'moment', MomentsViewSet)
router.register(r'rating', RatingViewSet)
router.register(r'review', ReviewViewSet)
router.register(r'review_like', ReviewLikeViewSet)
router.register(r'favorite', FavoriteViewSet)
router.register(r'favorite_movie', FavoritemovieViewSet)
router.register(r'history', HistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('movie/', MovieListAPIView.as_view(), name='movie-list'),
    path('movie/<int:pk>/', MovieDetailAPIView.as_view(), name='movie-detail'),
]