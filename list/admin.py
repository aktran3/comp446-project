from django.contrib import admin
from .models import Entry, List, Settings

admin.site.register(Entry)
admin.site.register(List)
admin.site.register(Settings)