from django.shortcuts import render
from rest_framework import viewsets
from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer

# Create your views here.
class DogViewSet(viewsets.ModelViewSet):       ##Note to self: ModelViewSet provides stuff like list, create, retrieve, update, and delete for us so we don’t need write each method by hand. It was ok in the lab but this one is much larger and would require a much longer code, I would've been stuck writing this for a long time!
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer