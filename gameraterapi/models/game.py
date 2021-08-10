from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    designer = models.CharField(max_length=100)
    year_released = models.IntegerField()
    number_of_players = models.IntegerField()
    duration = models.IntegerField()
    age_rec = models.IntegerField()




