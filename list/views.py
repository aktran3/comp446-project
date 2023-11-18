from django.shortcuts import render
from .models import Entry
from django.http import HttpResponse

def index(request):
    entry_list = Entry.objects.order_by('rating')
    context = {'entry_list': entry_list}
    return render(request, 'list/index.html', context)
