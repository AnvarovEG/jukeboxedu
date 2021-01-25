from django.db import models
from django.utils import timezone


class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, null=False)
    start_year = models.IntegerField(default=timezone.now().year, null=False)


class Track(models.Model):
    id = models.AutoField(primary_key=True)
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT, null=False, related_name='tracks')
    title = models.CharField(max_length=256, null=False)
    year = models.IntegerField(default=timezone.now().year, null=False)
    rate = models.FloatField(default=0, null=False)
    bpm = models.IntegerField(null=True)
    is_ep = models.BooleanField(default=False, null=False)


class Album(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField(default=timezone.now().year, null=False)
    title = models.CharField(max_length=128, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT, null=False, related_name='albums')
    tracks = models.ManyToManyField(Track)
