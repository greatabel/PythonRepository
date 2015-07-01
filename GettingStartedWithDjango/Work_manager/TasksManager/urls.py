from django.conf.urls import url

from django.views.generic.list import ListView
from django.views.generic import TemplateView

from TasksManager.models import Project, Task
from . import views
from TasksManager.views import MyView,GreetingView,ProjectList,TaskList

urlpatterns = [
    url(r'^project-detail-(?P<pk>\d+)$', views.project_detail, name="project_detail"),
    url(r'^$', views.index, name='index'),
    url(r'^indextest$', views.indextest, name='indextest'),
    url(r'^indexset$', views.indexset, name='indexset'),
    url(r'^indexQ$', views.indexQ, name='indexQ'),
    url(r'^connections$', views.connections, name='connections'),
    url(r'^create-developer$', views.create_developer,name='create_developer'),
    url (r'^project_list$', ListView.as_view(model=Project, template_name="TasksManager/project_list.html"), 
        name="project_list"),
    url (r'^task_detail_(?P<pk>\d+)$', views.task_detail, name='task_detail'),
    url(r'^about/', TemplateView.as_view(template_name="TasksManager/about.html")),
    url(r'^aboutA/', MyView.as_view()),
    url(r'^greeting/', GreetingView.as_view()),
    url(r'^projectlist/$', ProjectList.as_view()),
    url(r'^tasklist/$', TaskList.as_view()),
    url(r'^test/$', views.test, name="test"),

]