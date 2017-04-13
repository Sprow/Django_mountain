from django.conf.urls import url

from accounts.views import sign_out, sign_in


urlpatterns = [
    url(r'^logout/$', sign_out, name="logout"),
    url(r'^login/$', sign_in, name="login"),
]