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

    def __str__(self):
        return mark_safe("""
          <img src="{}{}" style="height: 200px; width: 300px;" />
        """.format(settings.MEDIA_URL, self.image))


class Results(models.Model):
    choices = models.ManyToManyField(Dummy)
