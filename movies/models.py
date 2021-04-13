from django.db import models


# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, default="brak")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return f"/aktor/{self.id}/"

    def delete_url(self):
        return f"/delete/person/{self.id}/"


class Movie(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.title} {self.year}"

    def get_absolute_url(self):
        return f"/movie/{self.id}/"
