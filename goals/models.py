from tabnanny import verbose
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Goal(models.Model):

    title = models.CharField(max_length=255, blank=False)
    note = models.TextField(max_length=2049, blank=True)

    def __str__(self):
        return self.title