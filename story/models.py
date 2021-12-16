from django.db import models

# Create your models here.

class Story(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return self.title[:20]