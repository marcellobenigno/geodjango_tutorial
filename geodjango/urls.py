from django.conf.urls import url, include
from django.contrib import admin

from .core import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^zoneamento/', include('geodjango.zoneamento_urbano.urls', namespace='zoneamento_urbano')),
    url(r'^mapa/', include('geodjango.basemap.urls', namespace='basemap')),
    url(r'^admin/', admin.site.urls),
]
