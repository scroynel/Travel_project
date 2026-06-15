from rest_framework import viewsets, exceptions
from .models import TravelProject, ProjectPlace
from .serializer import TravelProjectSerializer, ProjectPlaceSerializer


class TraveProjectViewSet(viewsets.ModelViewSet):
    queryset = TravelProject.objects.all()
    serializer_class = TravelProjectSerializer


class ProjectPlaceViewSet(viewsets.ModelViewSet):
    queryset = ProjectPlace.objects.all()
    serializer_class = ProjectPlaceSerializer
