from django.db import models
from accounts.models.users_models import UserMaster
from simple_history.models import HistoricalRecords


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateTimeField()
    max_attendees = models.IntegerField()
    attendees = models.ManyToManyField(UserMaster, related_name="events", blank=True)
    organizer = models.ForeignKey(
        UserMaster, on_delete=models.CASCADE, related_name="organized_events"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Creation Date",
        help_text="Date and time when the role was created.",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Update Date",
        help_text="Date and time when the role was last updated.",
    )
    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Deleted At",
        help_text="Date and time when the role was deleted.",
    )
    history = HistoricalRecords()

    def __str__(self):
        return self.title
    
    def available_slots(self):
        return self.max_attendees - self.attendees.count()