from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

#aici cream modelele in baza de date
#aici models extinde clasa model direct definita
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    page_count = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    date_created = models.DateTimeField(default=timezone.now())


    def __str__(self):
        return "{} by author, {} pages {}".format(self.title, self.author, self.page_count)

