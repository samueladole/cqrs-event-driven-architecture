from django.db import models
import uuid

class Event(models.Model):
    """Model representing an event in the event sourcing system."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    aggregate_id = models.UUIDField()
    aggregate_type = models.CharField(max_length=50)
    event_type = models.CharField(max_length=50)
    event_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta class for the Event model."""
        ordering = ["created_at"]
