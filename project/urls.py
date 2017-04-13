from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import home_page


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # django-wysiwyg-redactor
    url(r'^redactor/', include('redactor.urls')),

    url(r'^$', home_page, name="home"),

    url(r'^accounts/', include('accounts.urls')),
    url(r'^publications/', include('publications.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)