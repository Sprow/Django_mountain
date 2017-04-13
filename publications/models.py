from django.db import models
from accounts.models import User

from utils import get_file_path

from redactor.fields import RedactorField




class Publication(models.Model):
    title = models.CharField(max_length=255)
    # body = models.TextField()
    body = RedactorField(verbose_name=u'Text')
    image = models.FileField(upload_to=get_file_path)
    author = models.ForeignKey(User)
    added = models.DateTimeField(auto_now_add=True)
