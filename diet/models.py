from django.db import models


class Diet(models.Model):
    name = models.CharField(max_length=20)
    calories = models.IntegerField(primary_key=True)


