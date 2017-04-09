from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import home_page, sign_out, sign_in
from publications.views import publications

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', home_page, name="home"),

    url(r'^logout/$', sign_out, name="logout"),
    url(r'^login/$', sign_in, name="login"),

    url(r'^publications/$', publications, name="publications"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)