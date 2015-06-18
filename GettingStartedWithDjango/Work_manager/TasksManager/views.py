from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index (request) :
    # return HttpResponse ("Hello world!" )
    my_variable = "Hello world from abel"
    my_variable1 = "Hello world from abel\n test from abel"
    years_old = 29
    years_test = 1
    array_city_capitals = {"Paris","London"}
    returnV = {"my_variable1":my_variable1,"my_var": my_variable,"years_test":years_test,"years": years_old,"array_cities": array_city_capitals}
    return render(request, 'TasksManager/index.html', returnV)

def connections(request):
    import random
    i = random.randint(0,100)
    return render(request, 'TasksManager/connections.html',{"i":i})