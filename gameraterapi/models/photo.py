from django.db import models

class Photo(models.Model):
    image_url = models.CharField(max_length=150)
    caption = models.CharField(max_length=50)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)