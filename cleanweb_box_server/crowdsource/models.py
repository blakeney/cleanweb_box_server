from django.db import models
from django.utils import timezone
import datetime


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    points = models.CharField(max_length=100)

    def __unicode__(self):
        return str(self.username)+" "+str(self.points)

class Submission(models.Model):
    user = models.ForeignKey(User)
    IDno = models.PositiveIntegerField()
    picture = models.ImageField()
    sub_date = models.DateTimeField('date submitted')
    latitude = models.DecimalField()
    longitude = models.DecimalField()

    def __unicode__(self):
        return self.IDno
