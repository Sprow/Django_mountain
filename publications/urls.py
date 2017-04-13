from django.conf.urls import url

from publications.views import publications

urlpatterns = [
    url(r'^$', publications, name="publications"),
]