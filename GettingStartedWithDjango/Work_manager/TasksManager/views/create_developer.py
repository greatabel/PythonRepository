from django.shortcuts import render
from django.http import HttpResponse
from TasksManager.models import Supervisor, Developer

from django import forms

class Form_inscription(forms.Form):
    name  = forms.CharField(label="Name", max_length=30)
    login = forms.CharField(label="Login",max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    supervisor = forms.ModelChoiceField(label="Supervisor",
        queryset=Supervisor.objects.all())


def create_developer(request):
    supervisors_list = Supervisor.objects.all()
    if request.POST:
        form = Form_inscription(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            supervisor = form.cleaned_data['supervisor']

            new_developer = Developer(name=name,login=login,
                password=password, email="",supervisor=supervisor)
            new_developer.save()
            return HttpResponse("Developer added")
        else:
            
            return render(request, 'TasksManager/create_developer.html',{'form':form})
    else:
        form = Form_inscription()
        return render(request,'TasksManager/create_developer.html',{'form':form})

#    # View for create_developer
# def create_developer(request):
#     error = False
#      # If form has posted
#     if request.POST:
#     # This line checks if the data was sent in POST. If so, this means
#     #that the form has been submitted and we should treat it.
#         if 'name' in request.POST:
#            # This line checks whether a given data named name exists in the
#        #POST variables.
#             name = request.POST.get('name', '')
#        #       # This line is used to retrieve the value in the POST
#        # dictionary. Normally, we perform filters to recover the data to avoid
#        # false data, but it would have required many lines of code.
#         else:
#             error=True
#         if 'login' in request.POST:
#             login = request.POST.get('login', '')
#         else:
#             error=True
#         if 'password' in request.POST:
#             password = request.POST.get('password', '')
#         else:
#             error=True
#         if 'supervisor' in request.POST:
#             supervisor_id = request.POST.get('supervisor', '')
#         else:
#             error=True
#         if not error:
#                  # We must get the supervisor
#                 supervisor = Supervisor.objects.get(id = supervisor_id)
#                 new_dev = Developer(name=name, login=login, password=password,supervisor=supervisor)
#                 new_dev.save()
#                 return HttpResponse("Developer added")
#         else:
#                 return HttpResponse("An error as occured")
#     else:
#             supervisors_list = Supervisor.objects.all()
#             print(len(supervisors_list),supervisors_list[0].name)
#             return render(request, 'TasksManager/create_developer.html',{"supervisors_list": supervisors_list})
