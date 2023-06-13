import uuid

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    image = models.ImageField(upload_to='profile/')

    def __str__(self):
        return self.name