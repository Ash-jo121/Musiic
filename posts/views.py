# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404
from django.http import Http404
from .models import Album,Song

from django.shortcuts import render


def index(request):
    all_albums = Album.objects.all()
    context={'all_albums':all_albums}
    return render(request,'posts/index.html',context)


def detail(request,Album_id):
    try:
        album=Album.objects.get(id=Album_id)
    except Album.DoesNotExist:
        raise Http404("Album Does Not Exist")
    return render(request,'posts/detail.html',{'album':album})

def favorite(request,Album_id):
    album=get_object_or_404(Album,id=Album_id)
    try:
        selected_song=album.song_set.get(id=request.POST['song'])
    except(KeyError,Song.DoesNotExist):
        return render(request,'posts/detail.html',{
    'album':album,
    'error_message':"Song does not exit"
    })
    else:
        selected_song.is_favorite=True
        selected_song.save()
        return render(request,'posts/detail.html',{'album':album})

def display_favorites(request):
    all_albums=Album.objects.all()
    return render(request,'posts/display_favorites.html',{'all_albums':all_albums})

def remove_favorites(request):
    try:
        selected_song=song_set.get(id=request.POST['song'])
    except(KeyError,Song.DoesNotExist):
        return render(request,'posts/display_favorites.html',{
    'album':album,
    'error_message':'Song does not exist'
    })
    else:
        selected_song.is_favorite=False
        selected_song.save()
        return render(request,'posts/display_favorites.html',{'all_albums':all_albums})
    


# Create your views here.
