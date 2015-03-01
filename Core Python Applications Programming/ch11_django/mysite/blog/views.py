# views.py
from datetime import datetime
from django.http import HttpResponseRedirect
from blog.models import BlogPost
from django.views.generic import TemplateView
from django.conf.urls import patterns
from django.template import Context, loader
from django.http import HttpResponse

def archive(request):
    posts = BlogPost.objects.all()[:10]
    '''return direct_to_template(request, 'archive.html',
        {'posts': posts, 'form': BlogPostForm()})'''
    #TemplateView.as_view(template_name="archive.html")
    
    t = loader.get_template('archive.html')
    c = Context({
        'posts':posts,
    })
    return HttpResponse(t.render(c))

def create_blogpost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.timestamp = datetime.now()
            post.save()
    return HttpResponseRedirect('/blog/')

