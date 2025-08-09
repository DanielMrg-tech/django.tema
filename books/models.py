from django.db import models

# Create your models here.

#aici cream modelele in baza de date
#aici models extinde clasa model direct definita
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    page_count = models.IntegerField()