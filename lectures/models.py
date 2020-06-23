from django.db import models


# Create your models here.

class LectureVideos(models.Model):
    topic = models.CharField(max_length=50)
    disc = models.TextField()
    link = models.URLField(max_length=200)

    class Meta:
        verbose_name_plural = 'Topics'
