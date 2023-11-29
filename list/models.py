from django.db import models

class List(models.Model):
    listid = models.IntegerField()
    listname = models.CharField(max_length=500)
    userid = models.IntegerField()

class Entry(models.Model):
    title = models.CharField(max_length=500)
    rating = models.IntegerField()
    episodeCount = models.IntegerField()
    list = models.ForeignKey(List, on_delete=models.CASCADE)