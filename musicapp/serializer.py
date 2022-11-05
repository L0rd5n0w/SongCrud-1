from rest_framework import serializers
from .models import Artist,Lyric,Song


class ArtistSerial(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['first_name','last_name','age','id']


class LyricSerial(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = ['content','song_id','id']


class SongSerial(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['title','date_released','artist_id','id']