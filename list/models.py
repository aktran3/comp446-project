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
    isTelevision = models.BooleanField()
    seasonCount = models.IntegerField(null=True)
    episodeCount = models.IntegerField(null=True)
    entryid = models.IntegerField()
    currentSeason = models.IntegerField(null=True)
    currentEpisode = models.IntegerField(null=True)
    onlyEpisodes = models.BooleanField(null=True)

    runtime = models.IntegerField(null=True)
    releaseYear = models.IntegerField(null=True)

    list = models.ForeignKey(List, on_delete=models.CASCADE)