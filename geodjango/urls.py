from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'', include('geodjango.core.urls', namespace='core')),
    url(r'^mapa/', include('geodjango.basemap.urls', namespace='basemap')),
    url(r'^admin/', admin.site.urls),
]
