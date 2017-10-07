from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_page(request):
    # return HttpResponse('<html><title>To-Do lists</title></html>')
    if request.method == 'POST':
        return HttpResponse(request.POST['item_text'])
    return render(request, 'home.html')