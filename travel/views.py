from rest_framework import viewsets, exceptions
from .models import TravelProject, ProjectPlace
from .serializer import TravelProjectSerializer, ProjectPlaceSerializer


class TraveProjectViewSet(viewsets.ModelViewSet):
    queryset = TravelProject.objects.all()
    serializer_class = TravelProjectSerializer


    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.places.filter(visited=True).exists():
            raise exceptions.ValidationError(f'Cannot delete TravelProject {obj.name} with visited places')
        
        return super().destroy(request, *args, **kwargs)


class ProjectPlaceViewSet(viewsets.ModelViewSet):
    queryset = ProjectPlace.objects.all()
    serializer_class = ProjectPlaceSerializer
