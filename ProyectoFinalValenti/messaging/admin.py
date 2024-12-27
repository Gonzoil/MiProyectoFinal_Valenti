from django.contrib import admin
from .models import Message

# Register your models here.

admin.site.register(Message)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'subject', 'timestamp')
    search_fields = ('subject', 'content')
    list_filter = ('timestamp',)

