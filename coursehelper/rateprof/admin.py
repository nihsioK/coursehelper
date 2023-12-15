from django.contrib import admin

# Register your models here.
from .models import Professor, Rating

admin.site.register(Professor)
admin.site.register(Rating)
