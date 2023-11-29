from django.shortcuts import render
from django.db.models import Max
from .models import Entry, List
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotModified
from django.contrib.auth.models import User

# Acknowledgements: Referenced the Django docs
# Also referenced the login/logout tutorial from learndjango dot com when setting up accounts.

def index(request):
    if (request.user.is_authenticated):
        user_lists = List.objects.filter(userid=request.user.id)
        context = {'user_lists': user_lists}
        return render(request, 'list/userpage.html', context)
    else:
        return HttpResponse('user error, please log in.')

def create_list(request):
    if (request.user.is_authenticated):
        values = request.POST
        newListID = List.objects.all().aggregate(Max('listid')).get('listid__max') + 1
        newList = List(listname=values['title'], listid=newListID, userid=request.user.id)
        newList.save()
        return HttpResponseRedirect('/list/')
    else:
        return HttpResponse('user error, please log in.')

def list(request, id):
    if (request.user.is_authenticated):
        list_object = List.objects.get(listid=id)
        if (request.user.id == list_object.userid):
            entry_list = Entry.objects.filter(list__listid = id).order_by('rating')
            context = {'entry_list': entry_list, 'list_title': list_object.listname, 'list_id': id}
            return render(request, 'list/list.html', context)
        else:
            return HttpResponse("you can't view this list!")
    else:
        return HttpResponse('user error, please log in.')

def homepage(request):
    if (request.user.is_authenticated):
        return HttpResponseRedirect('/list/')
    else:
        return render(request, 'list/homepage.html')

def add_entry(request, id):
    values = request.POST
    newEntry = Entry(title=values['title'], rating=int(values['rating']), episodeCount=int(values['episodeCount']),
     list=List.objects.get(listid=id))
    newEntry.save()
    return HttpResponseRedirect('/list/' + str(id))

def new_user(request):
    if (request.user.is_authenticated):
        return HttpResponseRedirect('/list/')
    else:
        return render(request, 'list/newuser.html')

def create_user(request):
    if (request.method == "POST"):
        values = request.POST
        if (values['password'] == values['password_confirm']):
            user = User.objects.create_user(values['username'], None, values['password'])
            user.save()
            return HttpResponseRedirect('')
        else:
            print("oh no!")
            return HttpResponseRedirect('/new_user/')
    else:
        return render(request, 'list/homepage.html')
