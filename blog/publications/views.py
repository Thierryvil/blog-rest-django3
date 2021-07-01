from rest_framework import generics
from django_filters import rest_framework as filters
from .models import Publication
from .serializers import PublicationSerializer


class PublicationList(generics.ListCreateAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('author_id',)
