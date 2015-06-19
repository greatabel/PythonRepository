# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from TasksManager.models import Project ,Task,Supervisor,Developer


import random
# Create your views here.
def index (request) :
    # return HttpResponse ("Hello world!" )
    my_variable = "Hello world from abel"
    my_variable1 = "Hello world from abel\n test from abel"
    years_old = 29
    years_test = 1
    array_city_capitals = {"Paris","London"}

    # all_projects = Project.objects.all()
    # project_to_test = Project.objects.filter(client_name="test")
    project_to_test = Project.objects.filter(client_name="test")

    #测试queryset
    queryset_project = Project.objects.filter(client_name="test").order_by("id")
    frist_item_queryset = queryset_project[:1]
    project = frist_item_queryset.get()
    print("project=",project)

    #----end 测试queryset

    #只取一个
    first_project = Project.objects.get(id="1")
    print("first_project=",first_project)

    #--------------start 数据------
    i = random.randint(0,100)
    new_project = Project(title="Task Manager with Django"+str(i),
        description = "description test", client_name="test"+str(i))
    new_project.save()
    #--------------end --


    returnV = {"my_variable1":my_variable1,"my_var": my_variable,"years_test":years_test,"years": years_old,
    "array_cities": array_city_capitals,
    "action":'Display all project',
    "all_projects": project_to_test}
    return render(request, 'TasksManager/index.html', returnV)

def indextest(request):
    
    # Saving a new supervisor
    new_supervisor = Supervisor(name="Guido van Rossum", login="python",
   password="password", last_connection=timezone.now(), email="python@python.com", 
   specialisation="Python") # line 1
    new_supervisor.save()
     # Saving a new developer
    new_developer = Developer(name="Me", login="me", password="pass",
   last_connection=timezone.now(), email="me@python.com", supervisor=new_supervisor)
    new_developer.save()
     # Saving a new task
    project_to_link = Project.objects.get(id = 1) # line 2
    new_task = Task(title="Adding relation", description="Example of adding relation and save it", 
        time_elapsed=2, importance=0, project=project_to_link, app_user=new_developer) # line 3
    new_task.save()
    return render(request, 'TasksManager/indextest.html', {'action' : 'Save  relationship'})

def indexset(request):
    #修改的例子
    new_project = Project(title = "Other Project", description="try to update", client_name="People")
    new_project.save()
    task = Task.objects.get(id=11)
    task.description = "New description"
    task.project = new_project
    task.save()

    #更新一批 
    task1 = Project.objects.filter(client_name = "People").update(client_name="Nobody")
    
    #删除
    # one_task = Task.objects.get(id = 1)
    # one_task.delete() # line 1
    # all_tasks = Task.objects.all()
    # all_tasks.delete() # line 2
    
    return render(request, 'TasksManager/indexset.html', {'action' : 'update model'})

def connections(request):    
    i = random.randint(0,100)
    return render(request, 'TasksManager/connections.html',{"i":i})


def project_detail(request, pk):
    # return  HttpResponse("Hello world from detail!" +pk)
    project = Project.objects.get(id=pk)
    return render(request,'TasksManager/detail.html',locals())
