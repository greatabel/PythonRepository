from django.http import HttpResponse
from django.views.generic import View,ListView


from TasksManager.models import Project ,Task,Supervisor,Developer
#https://docs.djangoproject.com/en/1.8/topics/class-based-views/intro/

class MyView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse()

class GreetingView(View):
    greeting = "Good Day"

    def get(self, request):
        return HttpResponse(self.greeting)

class ProjectList(ListView):
    model = Project
    # project_list = Project.objects.all()
    # context_object_name = 'project_list'
    template_name = 'TasksManager/projectlist.html'

class TaskList(ListView):
    model = Task
    template_name = 'TasksManager/tasklist.html'