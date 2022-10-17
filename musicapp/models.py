from email.policy import default
from logging import PlaceHolder
from random import choices
from secrets import choice
from tkinter import CASCADE
from turtle import title
import uuid
from django.db import models
import uuid
from datetime import datetime
# Create your models here.


class Artist(models.Model):
    first_name = models.CharField(max_length=100 ,blank=True)
    last_name = models.CharField(max_length=100 , blank=True)
    age = models.IntegerField(blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.first_name


class Song(models.Model):
    title = models.CharField(blank=True, max_length=40)
    date_released = models.DateTimeField(blank=True, default=datetime.today)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    VOTE_TYPE = (
        ('likes', 'Like'),
        ('Dis', 'Dislike')
    )
    likes = models.CharField(max_length=50, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

class Lyric(models.Model):
    content = models.CharField(blank=True, max_length=5000)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.song_id.title