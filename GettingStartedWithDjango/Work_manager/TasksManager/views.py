from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index (request) :
    # return HttpResponse ("Hello world!" )
    my_variable = "abel"
    years_old = 29
    array_city_capitals = {"Paris","London"}
    returnV = {"my_var": my_variable,"years": years_old,"array_cities": array_city_capitals}
    return render(request, 'TasksManager/index.html', returnV)