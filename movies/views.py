from .serializers import MoviesSerializer
from .models import Movie
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status


# Create your views here.
class AddMovie(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer


class ListAllMovies(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = MoviesSerializer
    queryset = Movie.objects.all()


class MoviesByUser(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, *args, **kwargs):
        userId = request.data.get('userId')
        print(userId)
        user = User.objects.get(id=userId)
        movies = Movie.objects.filter(user = user)
        serializer = MoviesSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

