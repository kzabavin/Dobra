from django.db import models
from django.utils.translation import gettext_lazy as _

class FOLDERS(models.TextChoices):

    INBOX = 'ib', _('inbox')
    TODAY = 'td', _('today')
    NEXT = 'nx', _('next')
    TOMORROW = 'tm', _('tomorrow')
    SCHEDULED = 'sc', _('scheduled')
    SOMEDAY = 'sd', _('someday')
    WAITING = 'wf', _('waiting for')


class PRIORITY(models.IntegerChoices):

    LOW = -1, _('Low')
    MEDIUM = 0, _('Medium')
    HIGH = 1, _('High')
