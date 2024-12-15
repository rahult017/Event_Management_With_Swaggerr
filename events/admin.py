from django.contrib import admin
from events.models.event_models import Event
from simple_history.admin import SimpleHistoryAdmin

admin.site.register(Event,SimpleHistoryAdmin)
