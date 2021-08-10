from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator



class Rating(models.Model):
    stars = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)