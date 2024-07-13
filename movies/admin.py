from django.contrib import admin

# Register your models here.
from .models import Movies
# Register your models here.

@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    pass