from django.db import models

class Table(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=255)
    count = models.IntegerField()
    distance = models.IntegerField()

    def __str__(self):
        return self.title

class Genre(models.Model):
    name = models.CharField(max_length=255)

