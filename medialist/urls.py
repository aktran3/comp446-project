"""
URL configuration for medialist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from list import views as list_views

urlpatterns = [
    path('', list_views.homepage, name='homepage'),
    path('admin/', admin.site.urls),
    path('settings/', list_views.settings, name='settings'),
    path('update_settings/', list_views.update_settings, name='update_settings'),
    path('list/', list_views.index, name='index'),
    path('list/<int:id>', list_views.list, name='list'),
    path('list/<int:id>/add', list_views.add_entry, name='add_entry'),
    path('list/<int:id>/add_custom', list_views.add_custom_entry, name='add_custom_entry'),
    path('list/<int:id>/delete', list_views.delete_entry, name='delete_entry'),
    path('list/<int:id>/update/<int:season>/<int:episode>', list_views.update_place, name='update_place'),
    path('list/createnew', list_views.create_list, name='create_list'),
    path('', include("django.contrib.auth.urls")),
    path('new_user/', list_views.new_user, name='new_user'),
    path('new_user/create', list_views.create_user, name='create_user'),
]
