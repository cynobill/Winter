from django.db import models

# Create your models here.
from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Release(models.Model):
    title = models.CharField(max_length=100)
    #label = models.CharField(max_length=100,default='None')

    def __str__(self):
        return self.title


class Track(models.Model):
    title = models.CharField(max_length=100)
    release = models.ForeignKey(Release, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Target(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, related_name='targets', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Session(models.Model):
    url = models.CharField(max_length=500)
    start = models.DateTimeField()
    stop = models.DateTimeField()
    target = models.ForeignKey(Target, related_name='sessions', on_delete=models.CASCADE)
    def __str__(self):
        return self.start


class Hit(models.Model):
    time = models.DateTimeField()
    session = models.ForeignKey(Session, related_name='hit', on_delete=models.CASCADE)
    track = models.ForeignKey(Track, related_name='hit', on_delete=models.CASCADE)

    def __str__(self):
        return "Hit"#self.track.title #self.time.strftime('%H%M%S')+" "+
