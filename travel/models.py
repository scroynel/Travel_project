from django.db import models
import uuid


class TravelProject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    places = models.ManyToManyField('ProjectPlace')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProjectPlace(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    external_id = models.IntegerField()
    title = models.CharField(max_length=500)
    notes = models.TextField(blank=True)
    visited = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
