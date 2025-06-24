from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    release_year = models.IntegerField()
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to='song_images/', blank=True, null=True)  
    def __str__(self):
        return f"{self.artist} – {self.title}"
