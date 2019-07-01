from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Movie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    time_added = models.TimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title


