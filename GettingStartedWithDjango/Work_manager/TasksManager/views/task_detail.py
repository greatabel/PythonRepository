from django.shortcuts import render
from TasksManager.models import Task
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def task_detail(request, pk):
    check_task =  Task.objects.filter(id = pk)
    try:
        task = check_task.get()
    except (Task.DoesNotExist, Task.MultipleObjectsReturned):
        return HttpResponseRedirect(reverse('public_empty'))
        request.session['last_task'] = task.id
    return render(request, 'TasksManager/task_detail.html', {'object': task}) 