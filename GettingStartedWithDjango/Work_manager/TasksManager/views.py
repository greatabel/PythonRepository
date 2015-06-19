# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

from TasksManager.models import Project 

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

def connections(request):
    
    i = random.randint(0,100)
    return render(request, 'TasksManager/connections.html',{"i":i})