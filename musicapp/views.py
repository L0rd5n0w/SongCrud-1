from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Artist,Lyric,Song
from .serializer import ArtistSerial,LyricSerial,SongSerial
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

# Create your views here.


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def artist_list(request):
    if request.method == 'GET':
        artist = Artist.objects.all()
        serializer = ArtistSerial(artist, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArtistSerial(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def artist_prob(request, first_name):
    try:
        art = Artist.objects.get(first_name=first_name)
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArtistSerial(art)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArtistSerial(art, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        art.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def song_list(request):
    if request.method == 'GET':
        song = Song.objects.all()
        serializer = SongSerial(song, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SongSerial(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def song_prob(request, title):
    try:
        son = Song.objects.get(title=title)
    except Song.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SongSerial(son)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SongSerial(son, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        son.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def lyric_list(request):
    if request.method == 'GET':
        lyric = Lyric.objects.all()
        serializer = LyricSerial(lyric, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LyricSerial(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def lyric_prob(request, song_id):
    try:
        lyr = Lyric.objects.get(song_id=song_id)
    except Lyric.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LyricSerial(lyr)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LyricSerial(lyr, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        lyr.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
