from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .models import Professor, Rating
from .serializers import ProfessorSerializer, RatingSerializer


# Create your views here.

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

    @action(detail=True, methods=['get'])
    def ratings(self, request, pk=None):
        professor = self.get_object()
        ratings = Rating.objects.filter(professor=professor)
        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def perform_create(self, serializer):
        # You can add additional logic here before saving a Rating
        serializer.save()

