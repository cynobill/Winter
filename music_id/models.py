from django.db import models

# Create your models here.

class Release(models.Model):
    title = models.CharField(max_length=200)
    #acrc_id = models.CharField(max_length=20)
    #itunes_id = models.CharField(max_length=20)
    #spotify_id = models.CharField(max_length=20)
    def __str__(self):
        return self.title

class Artist(models.Model):
    name = models.CharField(max_length=200)
    #acrc_id = models.CharField(max_length=20)
    #itunes_id = models.CharField(max_length=20)
    #spotify_id = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=200)
    #acrc_id = models.CharField(max_length=20)
    #itunes_id = models.CharField(max_length=20)
    #spotify_id = models.CharField(max_length=20)
    release = models.ForeignKey(Release, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Channel(models.Model):
    site = models.CharField(max_length=200)
    channel = models.CharField(max_length=200)
    def __str__(self):
        return self.channel+"@"+self.site

class Session(models.Model):
    start = models.DateTimeField('time detection commenced')
    stop = models.DateTimeField('time detection ended',null=True)
    target = models.ForeignKey(Channel, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.start)

class Hit(models.Model):
    time = models.DateTimeField('time track was matched')
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.time)