from django.contrib import admin
from .models import Entry

# Register your models here.

class EntryAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'description', 'created']


admin.site.register(Entry, EntryAdmin)