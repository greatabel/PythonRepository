from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item


# Create your views here.
def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/')
    else:
        new_item_text = ''
    # item = Item()
    # item.text = request.POST.get('item_text', '')
    # item.save()
    # return HttpResponse('<html><title>To-Do lists</title></html>')
    return render(request, 'home.html')
