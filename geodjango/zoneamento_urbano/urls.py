from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^terrenos/$', views.terreno_list, name='terreno_list'),
    url(r'^novo-terreno/$', views.terreno_new, name='terreno_new'),
    url(r'^(?P<pk>\d+)/editar-terreno/$', views.terreno_edit, name='terreno_edit'),
    # url(r'^(?P<pk>\d+)/deletar-barragem/$', views.BarragemDelete.as_view(), name='barragem_delete'),
]
