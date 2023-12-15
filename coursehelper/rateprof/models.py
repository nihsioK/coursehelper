from django.db import models


# Create your models here.


class Professor(models.Model):
    name = models.CharField(max_length=100)
    school = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Rating(models.Model):
    professor = models.ForeignKey(Professor, related_name='ratings', on_delete=models.CASCADE)
    grade_received = models.FloatField()
    user_comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.professor.name} - {self.grade_received}"
