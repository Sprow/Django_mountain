from django.db import models

from django.contrib.auth.models import AbstractUser

from utils import get_file_path


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    photo = models.FileField(upload_to=get_file_path)
    birth_date = models.DateField(blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        swappable = 'AUTH_USER_MODEL'

class WebsiteSettings(models.Model):
    title = models.CharField(max_length=255)
    favicon = models.FileField(upload_to=get_file_path, blank=True, null=True)
    descript = models.TextField()
