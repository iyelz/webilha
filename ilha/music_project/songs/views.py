from django.shortcuts import render
from .models import Song

def index(request):
    songs = Song.objects.all()
    return render(request, 'songs/index.html', {'songs': songs})
