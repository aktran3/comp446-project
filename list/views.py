from django.shortcuts import render
from django.db.models import Max
from .models import Entry, List, Settings
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotModified, JsonResponse
from django.contrib.auth.models import User
import requests
import re
import types

# Acknowledgements: Referenced the Django docs, and MDN web docs
# Also referenced the login/logout tutorial from learndjango dot com when setting up accounts.
# Referenced wikimedia REST api docs and user-agent policy.
# Referenced python requests module docs, and the python docs

headers = {'UPDATE WITH USER AGENT'}
# This sets up the user agent, which is required for wikimedia apis.
# The wikipedia REST API is licensed under https://creativecommons.org/licenses/by-sa/4.0/deed.en


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
        newListID = List.objects.all().aggregate(Max('listid')).get('listid__max')
        if newListID == None:
            newListID = 1
        else:
            newListID = newListID + 1
        newList = List(listname=values['title'], listid=newListID, userid=request.user.id)
        newList.save()
        return HttpResponseRedirect('/list/')
    else:
        return HttpResponse('user error, please log in.')

def list(request, id):
    if (request.user.is_authenticated):
        list_object = List.objects.get(listid=id)
        if (request.user.id == list_object.userid):
            entry_list = Entry.objects.filter(list__listid = id).order_by('title')
            context = {'entry_list': entry_list, 'list_title': list_object.listname, 'list_id': id}
            return render(request, 'list/list.html', context)
        else:
            return HttpResponseRedirect('/list/')
    else:
        return HttpResponse('user error, please log in.')

def homepage(request):
    if (request.user.is_authenticated):
        return HttpResponseRedirect('/list/')
    else:
        return render(request, 'list/homepage.html')

def add_custom_entry(request, id):
    values = request.POST
    newEntryID = Entry.objects.all().aggregate(Max('entryid')).get('entryid__max')
    if (newEntryID == None):
        newEntryID = 1
    else:
        newEntryID = newEntryID + 1
    if (values['seasonCount'] == ""):
        customSeasonCount = 1
    else:
        customSeasonCount = int(values['seasonCount'])
    if (values.get('onlyEpisodes') != None):
        justEpisodes = True
    else:
        justEpisodes = False
    newEntry = Entry(title=values['title'], seasonCount=customSeasonCount, episodeCount=int(values['episodeCount']),
    list=List.objects.get(listid=id), entryid=newEntryID, currentEpisode=1, currentSeason=1, onlyEpisodes=justEpisodes)
    newEntry.save()
    return HttpResponseRedirect('/list/' + str(id))

def add_entry(request, id):
    defaultcountry = Settings.objects.get(userid=request.user.id).defaultcountry

    requestTitle = str(request.body).removeprefix("b'").removeprefix('b"').removesuffix("'").removesuffix('"')
    requestTitle = requestTitle.replace(':','%3A').replace('(','%28').replace(')','%29').replace('?','%3F').replace('!','%21').replace(" ", "_")
    # percent-encoding
    requestURL = "https://en.wikipedia.org/api/rest_v1/page/html/" + requestTitle
    requestHTML = requests.get(requestURL, headers=headers).text
    
    foundTitle = re.search("<title>&lt;i>(.*?)&lt;", str(requestHTML))
    foundEpisodes = re.search("\"num_episodes\":\{\"wt\":\"(&lt;onlyinclude>)*(\d)+", str(requestHTML))
    if foundTitle == None or foundEpisodes == None:
        # this first block of code accounts for shows that share names with other articles
        requestURL = "https://en.wikipedia.org/api/rest_v1/page/html/" + requestTitle + "_%28TV_series%29"
        requestHTML = requests.get(requestURL, headers=headers).text
        foundTitle = re.search("<title>&lt;i>(.*?)&lt;", str(requestHTML))  
        if foundTitle == None or re.search("<title>&lt;i>(.*?)&lt;/i> \(franchise\)", str(requestHTML)) != None:
            # this second block of code searches for shows under the user's default country parameter
            # this is useful for shows that have multiple versions across different countries with the same title
            requestURL = "https://en.wikipedia.org/api/rest_v1/page/html/" + requestTitle + "_%28" + defaultcountry +"_TV_series%29"
            requestHTML = requests.get(requestURL, headers=headers).text
            foundTitle = re.search("<title>&lt;i>(.*?)&lt;", str(requestHTML)).group()
        else:
            foundTitle = foundTitle.group()
    else:
        foundTitle = foundTitle.group()
    foundTitle = foundTitle.replace("<title>&lt;i>", "")
    foundTitle = foundTitle.replace("&lt;", "")

    foundEpisodes = re.search("\"num_episodes\":\{\"wt\":\"(&lt;onlyinclude>)*(\d|,)+", str(requestHTML)).group()
    foundEpisodes = foundEpisodes.replace("\"num_episodes\":{\"wt\":\"", "").replace("&lt;onlyinclude>", "").replace(",", "")
    foundEpisodes = int(foundEpisodes)

    foundSeasons = re.search("\"(num_series|num_seasons)\":\{\"wt\":\"(\d)+", str(requestHTML)).group()
    foundSeasons = foundSeasons.replace("\"num_series\":{\"wt\":\"", "")
    foundSeasons = foundSeasons.replace("\"num_seasons\":{\"wt\":\"", "")
    foundSeasons = int(foundSeasons)

    newEntryID = Entry.objects.all().aggregate(Max('entryid')).get('entryid__max')
    if (newEntryID == None):
        newEntryID = 1
    else:
        newEntryID = newEntryID + 1
    newEntry = Entry(title=foundTitle, seasonCount=foundSeasons, episodeCount=foundEpisodes, 
    list=List.objects.get(listid=id), entryid=newEntryID, currentEpisode=1, currentSeason=1, onlyEpisodes=False)
    newEntry.save()
    return JsonResponse({"title": foundTitle, "episodes": foundEpisodes, "seasons": foundSeasons, "entryID": newEntryID})
    # return JsonResponse({"title": "what", "episodes": 2, "seasons": 1})

def delete_entry(request, id):
    Entry.objects.get(entryid=int(str(request.body).removeprefix("b'").removesuffix("'"))).delete()
    return JsonResponse({"removed_id": int(str(request.body).removeprefix("b'").removesuffix("'"))})

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
            userSettings = Settings(userid = user.id, defaultcountry = values['country'].capitalize())
            userSettings.save()
            return HttpResponseRedirect('')
        else:
            return HttpResponseRedirect('/new_user/')
    else:
        return render(request, 'list/homepage.html')

def settings(request):
    if(request.user.is_authenticated):
        userSettings = Settings.objects.get(userid=request.user.id)
        context = {"current_settings": userSettings}
        return render(request, 'list/settings.html', context)
    else:
        return render(request, 'list/settings.html')

def update_settings(request):
    if(request.user.is_authenticated):
        values = request.POST
        userSettings = Settings.objects.get(userid=request.user.id)
        userSettings.defaultcountry = values['country'].capitalize()
        userSettings.save()
        context = {"current_settings": userSettings}
        return render(request, 'list/settings.html', context)
    else:
        return render(request, 'list/settings.html')

def update_place(request, id, season, episode):
    if(request.user.is_authenticated):
        updatedEntry = Entry.objects.get(entryid=int(str(request.body).removeprefix("b'").removesuffix("'")))
        updatedEntry.currentSeason = season
        updatedEntry.currentEpisode = episode
        updatedEntry.save()
        return JsonResponse({"new_season": season, "new_episode": episode})
    else:
        return render(request, 'list/homepage.html')
