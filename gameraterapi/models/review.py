from django.db import models


class Review(models.Model):
    review_text = models.TextField((""))
    game = models.ForeignKey("Game", default=0, on_delete=models.CASCADE)
    player = models.ForeignKey("Player", default=0, on_delete=models.CASCADE)