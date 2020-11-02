from django.db import models
from django.contrib.auth.models import User

class Url(models.Model):
    actualurl = models.CharField(max_length=500)
    shortenedid = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return '{} to {}'.format(self.actualurl, self.shortenedid)