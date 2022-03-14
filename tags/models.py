from tabnanny import verbose
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    title = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag_detail', args=[str(self.id)])
