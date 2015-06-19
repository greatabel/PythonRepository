from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^project-detail-(?P<pk>\d+)$', views.project_detail, name="project_detail"),
    url(r'^$', views.index, name='index'),
    url(r'^indextest$', views.indextest, name='indextest'),
    url(r'^indexset$', views.indexset, name='indexset'),
    url(r'^connections$', views.connections, name='connections'),

]