from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'uploaded_by', 'course', 'semester', 'description', 'pdf_file', 'tags']
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['uploaded_by'] = instance.uploaded_by.username  # or any other attribute of User
        representation['course'] = instance.course.title  # or any other attribute of Course
        representation['semester'] = instance.semester.name  # or any other attribute of Semester
        representation['tags'] = [tag.name for tag in instance.tags.all()]  # List of tag names
        return representation
