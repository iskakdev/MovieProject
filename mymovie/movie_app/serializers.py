from rest_framework import serializers
from .models import (Profile, Country, Director, Actor,
                     Genre, Movie, MovieLanguages, Moments,
                     Rating, Favorite, FavoriteMovie, History)
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'age',
                  'phone_number', 'status']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Profile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['director_name']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_name']


class MovieListSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format='%Y')
    country = CountrySerializer(many=True)
    genre = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'movie_image', 'movie_name', 'year',
                  'country', 'genre', 'status_movie']


class CountryDetailSerializer(serializers.ModelSerializer):
    country_movie = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['country_name', 'country_movie']


class DirectorDetailSerializer(serializers.ModelSerializer):
    director_movie = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = Director
        fields = ['director_name', 'bio', 'age',
                  'director_image', 'director_movie']


class ActorDetailSerializer(serializers.ModelSerializer):
    actor_movie = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ['actor_name', 'bio', 'age',
                  'actor_image', 'actor_movie']


class GenreDetailSerializer(serializers.ModelSerializer):
    genre_movie = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = ['genre_name', 'genre_movie']


class MomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = ['movie_moments']


class MovieLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['language', 'video']


class RatingSerializer(serializers.ModelSerializer):
    user = ProfileRatingSerializer()
    created_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    class Meta:
        model = Rating
        fields = ['id', 'user', 'parent', 'stars', 'text', 'created_date']


class MovieDetailSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format='%d-%m_Y')
    country = CountrySerializer(many=True)
    genre = GenreSerializer(many=True)
    director = DirectorSerializer(many=True)
    actor = ActorSerializer(many=True)
    movie_frames = MomentsSerializer(many=True, read_only=True)
    movie_language = MovieLanguagesSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)
    get_avg_rating = serializers.SerializerMethodField()
    get_count_people = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'year', 'country',
                  'director', 'actor', 'genre', 'types',
                  'movie_time', 'description', 'movie_trailer',
                  'movie_image', 'status_movie', 'movie_frames',
                  'movie_language', 'ratings', 'get_avg_rating',
                  'get_count_people']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating

    def get_count_people(self, obj):
        return obj.get_count_people


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'