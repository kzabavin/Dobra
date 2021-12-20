from django.db import models
from django.utils.translation import gettext_lazy as _
from .consts import FOLDERS, PRIORITY


class Tag(models.Model):
    title = models.CharField(max_length=255, blank=False)


class Context(models.Model):

    title = models.CharField(max_length=255, blank=False)


class Goal(models.Model):
    
    title = models.CharField(max_length=255, blank=False)
    note = models.TextField(max_length=2049, blank=True)


class Group(models.Model):

    """Goups of contacts"""

    groupname = models.CharField(max_length=255)


class Contact(models.Model):
    email = models.EmailField()
    nickname = models.CharField(max_length=255, blank=True)

    birhday = models.DateField(blank=True)
    description = models.TextField(max_length=2049, blank=True)

    phone = models.CharField(
        verbose_name=_('Phone'),
        max_length=20,
        blank=True,
        null=True,
    )
    """Phone number"""

    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL, blank=True, null=True)
    """Group"""


class Repeat(models.Model):

    DAILY = 1
    WEEKLY = 2
    WEEKDAY = 3
    MONTHLY = 4
    YEARLY = 5

    MODE = [
        (DAILY, _("daily")),
        (WEEKLY, _("weekly")),
        (WEEKDAY, _("weekday")),
        (MONTHLY, _("monthly")),
        (YEARLY, _("yearly"))
    ]

    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 0

    WEEKDAYS = [
        (MON, _('monday')),
        (TUE, _('tuesday')),
        (WED, _('wednesday')),
        (THU, _('thursday')),
        (FRI, _('friday')),
        (SAT, _('saturday')),
        (SUN, _('sunday'))
    ]

    frequency = models.DecimalField(blank=True, max_digits=5, decimal_places=0)

    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)

    monthly_day = models.BooleanField(default=False)
    monthly_date = models.BooleanField(default=False)

    period_start = models.DateField(blank=True)
    period_end = models.DateField(blank=True)

    mode = models.IntegerField(
        choices=MODE,
        default=DAILY,
        blank=False,
        null=True
    )

    monthly_o = models.IntegerField(
        choices=[(1, 'first'), (2, 'second'), (3, 'third'),
                 (4, 'fourth'), (-1, 'last')],
        default=1
    )

    monthly_w = models.IntegerField(
        choices=WEEKDAYS,
        default=MON
    )

    monthly_type = models.IntegerField(
        choices=[(i, str(i)) for i in range(1, 32)]
    )


class Project(models.Model):

    title = models.CharField(max_length=255, blank=False)
    note = models.TextField(max_length=2049, blank=True)
    
    start_time = models.DateTimeField(auto_now_add=True)
    """ today 
        next if blank
        tomorrow 
        sceduled other """

    context = models.ForeignKey(
        Context, on_delete=models.SET_NULL, blank=True, null=True)

    goal = models.ForeignKey(
        Goal, on_delete=models.SET_NULL, blank=True, null=True)

    deadline = models.DateTimeField(blank=True)
    compleat = models.BooleanField(default=False)
    trashed = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)


class Task(models.Model):

    title = models.CharField(max_length=255, blank=False)
    note = models.TextField(max_length=2049, blank=True)
    start_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True)
    compleat = models.BooleanField(default=False)
    trashed = models.BooleanField(default=False)

    folder = models.CharField(
        choices=FOLDERS.choices, default=FOLDERS.INBOX, blank=False,
        max_length=2)
    priority = models.IntegerField(
        choices=PRIORITY.choices, default=PRIORITY.MEDIUM, blank=False)

    context = models.ForeignKey(
        Context, on_delete=models.SET_NULL, blank=True, null=True)
    assign = models.ForeignKey(
        Contact, on_delete=models.SET_NULL, blank=True, null=True)
    goal = models.ForeignKey(
        Goal, on_delete=models.SET_NULL, blank=True, null=True)
    project = models.ForeignKey(
        Project, on_delete=models.SET_NULL, blank=True, null=True)
    repeate = models.ForeignKey(
        Repeat, on_delete=models.SET_NULL, blank=True, null=True)
    tags = models.ManyToManyField(
        Tag, blank=True)


class Reminder(models.Model):

    task_id = models.ForeignKey(
        Task, on_delete=models.CASCADE, blank=False, null=False)

    reminder_type = models.IntegerField(
        choices=[(1, 'Popup'), (2, 'E-mail')],
        default=1
    )

    reminder_value = models.DecimalField(blank=True, max_digits=4, decimal_places=0)
    """ not for unit = 'ondate' """

    unit = models.CharField(
        choices=[('minutes', 'minutes'), ('hours', 'hours'), ('days', 'days'),
                 ('ondate', 'on date')
                 ],
        default='minutes',
        max_length=10
    )

    ondate = models.DateTimeField(blank=True)
    """ only for unit = 'ondate' """


class Subtask(models.Model):

    title = models.CharField(max_length=255, blank=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, blank=False)


class Comment(models.Model):

    comment = models.TextField(max_length=2049, blank=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, blank=False)

