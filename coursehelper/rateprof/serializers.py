from django.db import models
from rest_framework import serializers
from .models import Professor, Rating
from django.db.models import Avg, FloatField
from django.db.models.functions import Cast


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'professor', 'grade_received', 'user_comment']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['professor'] = instance.professor.name  # Displaying professor's name
        return representation


class ProfessorSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True, read_only=True)
    average_grade = serializers.SerializerMethodField()

    class Meta:
        model = Professor
        fields = ['id', 'name', 'school', 'ratings', 'average_grade']

    def get_average_grade(self, obj):
        if obj.ratings.count() > 0:
            return obj.ratings.annotate(numeric_grade=Cast('grade_received', FloatField())).aggregate(Avg('numeric_grade'))['numeric_grade__avg']
        return None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['school'] = instance.school  # or any other attribute you want to add
        # You can customize the representation of ratings or average_grade here if needed
        return representation
