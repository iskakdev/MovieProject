from django.urls import path, include
from .views import (ProfileViewSet, CountryViewSet, DirectorViewSet,
                    ActorViewSet, GenreViewSet, MovieViewSet,
                    MovieLanguagesViewSet, RatingViewSet,
                    FavoriteViewSet, FavoriteMovieViewSet,
                    HistoryViewSet, RegisterView, CustomLoginView,
                    LogoutView)
from rest_framework import routers
router = routers.SimpleRouter()

router.register(r'profile', ProfileViewSet)
router.register(r'country', CountryViewSet)
router.register(r'director', DirectorViewSet)
router.register(r'actor', ActorViewSet)
router.register(r'genre', GenreViewSet)
router.register(r'movie', MovieViewSet)
router.register(r'movie_languages', MovieLanguagesViewSet)
router.register(r'rating', RatingViewSet)
router.register(r'favorite', FavoriteViewSet)
router.register(r'favorite_movie', FavoriteMovieViewSet)
router.register(r'history', HistoryViewSet)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register_list'),
    path('login/', CustomLoginView.as_view(), name='login_list'),
    path('logout/', LogoutView.as_view(), name='logout_list'),

    path('', include(router.urls))
]