from django.urls import path, include
from .views import (ProfileViewSet, CountryAPIView, CountryDetailView, DirectorAPIView,
                    DirectorDetailView, ActorAPIView, ActorDetailView,
                    GenreAPIView, GenreDetailView,
                    MovieListAPIView, MovieDetailAPIView,
                    MovieLanguagesViewSet, MomentsViewSet, RatingViewSet,
                    FavoriteViewSet, FavoriteMovieViewSet,
                    HistoryViewSet, RegisterView, CustomLoginView,
                    LogoutView)
from rest_framework import routers
router = routers.SimpleRouter()

router.register(r'profile', ProfileViewSet)
router.register(r'movie_languages', MovieLanguagesViewSet)
router.register(r'moments', MomentsViewSet)
router.register(r'rating', RatingViewSet)
router.register(r'favorite', FavoriteViewSet)
router.register(r'favorite_movie', FavoriteMovieViewSet)
router.register(r'history', HistoryViewSet)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register_list'),
    path('login/', CustomLoginView.as_view(), name='login_list'),
    path('logout/', LogoutView.as_view(), name='logout_list'),
    path('', include(router.urls)),

    path('movie/', MovieListAPIView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailAPIView.as_view(), name='movie_detail'),
    path('country/', CountryAPIView.as_view(), name='country_list'),
    path('country/<int:pk>/', CountryDetailView.as_view(), name='country_detail'),
    path('director/', DirectorAPIView.as_view(), name='director_list'),
    path('director/<int:pk>/', DirectorDetailView.as_view(), name='director_detail'),
    path('actor/', ActorAPIView.as_view(), name='actor_list'),
    path('actor/<int:pk>/', ActorDetailView.as_view(), name='actor_detail'),
    path('genre/', GenreAPIView.as_view(), name='genre_list'),
    path('genre/<int:pk>/', GenreDetailView.as_view(), name='genre_detail')
]