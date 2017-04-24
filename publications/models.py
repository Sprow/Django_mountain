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

    def __str__(self):
        return str(self.author) + " id " + str(self.id)

    def get_likes_count(self):
        return PublicationLike.objects.filter(publication=self).count()

    # def get_all_comments(self):
    #     return PublicationComment.objects.all()


class PublicationLike(models.Model):
    publication = models.ForeignKey(Publication)
    user = models.ForeignKey(User)


class PublicationComment(models.Model):
    publication = models.ForeignKey(Publication, related_name="comments")
    user = models.ForeignKey(User)
    comment = models.TextField()
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[:30]
