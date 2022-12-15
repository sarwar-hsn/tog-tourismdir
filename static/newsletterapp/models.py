import uuid
from django.db import models
from datetime import datetime


# Create your models here.
class Newsletter(models.Model):
    tracking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=254,unique=True)
    created_at = models.DateTimeField(auto_now=True,editable=False)
    isSubscribed = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.email}-{self.tracking_id}"
    



