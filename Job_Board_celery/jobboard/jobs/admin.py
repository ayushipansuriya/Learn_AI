from django.contrib import admin
from .models import Job, Subscriber

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'skill', 'location', 'created_at')
    search_fields = ('title', 'skill', 'location')
    list_filter = ('location', 'skill')
    ordering = ('-created_at',)

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'skill', 'location')
    search_fields = ('email', 'skill', 'location')
    list_filter = ('skill', 'location')
