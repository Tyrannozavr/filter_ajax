from django.db import models

class Table(models.Model):
    title = models.CharField(max_length=255)


class Genre(models.Model):
    name = models.CharField(max_length=255)

