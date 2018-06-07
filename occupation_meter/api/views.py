from django.shortcuts import render

from rest_framework import generics
from .serializers import CountRequestSerializer
from .models import CountRequest
from.utils import download_image

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = CountRequest.objects.all()
    serializer_class = CountRequestSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new count_request."""
        count_request = serializer.save()
        download_image(count_request=count_request)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = CountRequest.objects.all()
    serializer_class = CountRequestSerializer
