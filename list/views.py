from django.shortcuts import render
from .models import Entry
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    entry_list = Entry.objects.order_by('rating')
    context = {'entry_list': entry_list}
    return render(request, 'list/index.html', context)

def add_entry(request):
    values = request.POST
    newEntry = Entry(title=values['title'], rating=int(values['rating']), episodeCount=int(values['episodeCount']))
    newEntry.save()
    return HttpResponseRedirect('/list/')
