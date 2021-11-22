from django.db import models

# Our tables

class Tasks(models.Model):
    INBOX="in"
    TODAY="td" 
    NEXT="nx"
    TOMORROW="tm"
    SCHEDULED="sc"
    SOMEDAY="sd"
    WAITING="wf"
    
    FOLDERS=[
        (INBOX, "inbox"),
        (TODAY="today"),
        (NEXT="next"),
        (TOMORROW="tomorrow"),
        (SCHEDULED="scheduled")
        (SOMEDAY="someday"),
        (WAITING="waiting for")
    ]
    title = models.CharField(max_length=255)
    notes = models.TextField(max_length=2049, blank=True)
    start_time = models.DateTimeField(auto_now_add=true)
    deadline = models.DateTimeField(blank=True)
    complet = models.BooleanField(default=False)
    trashed = models.BooleanField(default=False)
    folder = models.CharField(
            choices=FOLDERS, 
            default=INBOX
    )

class Subtasks(models.Model):
    title = models.CharField(max_length=255)

class Comments(models.Model):
    comment = models.TextField(max_length=2049)

class Projects(models.Model):
    title = models.CharField(max_length=255)
    notes = models.TextField(max_length=2049, blank=True)
    start_time = models.DateTimeField(auto_now_add=true)
    deadline = models.DateTimeField(blank=True)
    complet = models.BooleanField(default=False)
    trashed = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)

class Goals(models.Model):
    title = models.CharField(max_length=255)

class Contacts(models.Model):
    email = models.EmailField()
    nickname = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    birhday = models.DateField(blank=True)
    description = models.TextField(max_length=2049, blank=True)

class Groups(models.Model):
    groupname = models.CharField(max_length=255)

class Repeates(models.Model):
    frequency = models.DecimalField(blank=True)
    
    monday = models.BooleanField(default=False) 
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)
    
    period_start = models.DateField(blank=True)
    period_end = models.DateField(blank=True)
