from tkinter import CASCADE
import uuid
from django.db import models
import uuid
from datetime import datetime
# Create your models here.


class Artist(models.Model):
    first_name = models.CharField(max_length=100 ,blank=True)
    last_name = models.CharField(max_length=100 , blank=True)
    age = models.IntegerField(blank=True)
    id = models.UUIDField(default=uuid.uuid3, unique=True, primary_key=True, editable=False)


class Song(models.Model):
    title = models.CharField(blank=True, max_length=40)
    date_released = models.DateTimeField(blank=True, auto_now_add=True)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    VOTE_TYPE = (
        ('likes', 'Like'),
        ('Dis', 'Dislike')
    )
    id = models.UUIDField(default=uuid.uuid3, unique=True, primary_key=True, editable=False)

class Lyric(models.Model):
    content = models.CharField(blank=True, max_length=5000)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid3, unique=True, primary_key=True, editable=False)