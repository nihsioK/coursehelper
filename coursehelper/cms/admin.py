from django.contrib import admin

# Register your models here.
from .models import Course, Semester, Tag, Note

admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(Tag)
admin.site.register(Note)

