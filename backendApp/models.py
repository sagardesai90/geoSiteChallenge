from django.db import models
from uuid import uuid4

from django.contrib.auth.models import User

# Create your models here.
class RequestsMade(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True)
    last_modified = models.DateTimeField(auto_now=True)

class PersonalRequests(RequestsMade):
    user = models.ForeignKey(User, on_delete=models.CASCADE)