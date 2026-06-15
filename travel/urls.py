from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('travels', views.TraveProjectViewSet)
router.register('places', views.ProjectPlaceViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
