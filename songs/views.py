from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from albums.models import Album
from rest_framework import generics
from django.shortcuts import get_object_or_404


class SongView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SongSerializer
    queryset = Song.objects.all()
    # caso na url não tivesse com o valor pk, seria necessario passar isso:
    # lookup_url_kwarg = "album_id" -> para o get dentro da classe saiba qual o parametro estamos procurando
    def perform_create(self, serializer):
        # self.__dict__
        # A melhor forma para de bugar uma instacia de classe
        album = get_object_or_404(Album, pk=self.kwargs["pk"])
        serializer.save(album=album)

