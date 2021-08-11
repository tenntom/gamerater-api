from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator



class Rating(models.Model):
    stars = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    game = models.ForeignKey("Game", default=0, on_delete=models.CASCADE)
    player = models.ForeignKey("Player", default=0, on_delete=models.CASCADE)
