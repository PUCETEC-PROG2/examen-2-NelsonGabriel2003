from django.db import models

# Create your models here.
class Movies (models.Model):
    publication_date = models.CharField(max_length=30, null=False)
    director = models.CharField(max_length=30, null=False)
    gender = models.CharField(max_length=30, null=False)
    synopsis = models.TextField(null=False)
    
    def __str__(self) -> str:
        return self.name 