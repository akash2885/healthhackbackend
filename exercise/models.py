from django.db import models


class Exercise(models.Model):
    name = models.CharField(max_length=20)
    weight = models.CharField(max_length=5)
    reps = models.IntegerField()
    sets = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name
