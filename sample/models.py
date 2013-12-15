from os.path import join
from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe


class DummyManager(models.Manager):

    def get_active(self):
        return self.all()


class Dummy(models.Model):
    image = models.FileField(upload_to='images')

    objects = DummyManager()


class Results(models.Model):
    choices = models.ManyToManyField(Dummy)
