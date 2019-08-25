# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Album(models.Model):
    Album_title=models.CharField( max_length=250)
    Artist=models.CharField(max_length=250)
    Album_logo=models.CharField(max_length=250)
    Genre=models.CharField(max_length=250)

    def __str__(self):
        return self.Album_title+"--"+self.Artist

    

class Song(models.Model):
    album=models.ForeignKey("Album", on_delete=models.CASCADE)
    song_name=models.CharField(max_length=250)
    file_type=models.CharField(max_length=50)
    is_favorite=models.BooleanField(default=False)

    def __str__(self):
        return self.song_name
    