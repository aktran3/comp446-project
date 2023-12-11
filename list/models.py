from django.db import models

class Settings(models.Model):
    userid = models.IntegerField()
    defaultcountry = models.CharField(max_length=500)

class List(models.Model):
    listid = models.IntegerField()
    listname = models.CharField(max_length=500)
    userid = models.IntegerField()

class Entry(models.Model):
    title = models.CharField(max_length=500)
    seasonCount = models.IntegerField()
    episodeCount = models.IntegerField()
    entryid = models.IntegerField()
    currentSeason = models.IntegerField()
    currentEpisode = models.IntegerField()
    onlyEpisodes = models.BooleanField()
    list = models.ForeignKey(List, on_delete=models.CASCADE)