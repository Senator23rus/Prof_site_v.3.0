
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from general.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  include('general.urls')),
    path('home/', include('general.urls')),
    path('news/', news, name='news'),
]

#if settings.DEBUG:
   #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_Root)