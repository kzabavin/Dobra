from tabnanny import verbose
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from Dobra.consts import FOLDERS, PRIORITY
from datetime import date, datetime, timedelta

from goals.models import Goal
from contexts.models import Context


class Project(models.Model):

    title = models.CharField(max_length=255, blank=False)
    note = models.TextField(max_length=2049, blank=True)

    start_time = models.DateTimeField(blank=True, null=True)
    """ today 
        next if blank
        tomorrow 
        sceduled other """

    context = models.ForeignKey(
        Context, on_delete=models.SET_NULL, blank=True, null=True)

    goal = models.ForeignKey(
        Goal, on_delete=models.SET_NULL, blank=True, null=True)

    deadline = models.DateTimeField(blank=True, null=True)
    compleat = models.BooleanField(default=False)
    trashed = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.title

