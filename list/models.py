from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=500)
    rating = models.IntegerField()
    episodeCount = models.IntegerField()
    avgEpisodeLength = models.DurationField()
