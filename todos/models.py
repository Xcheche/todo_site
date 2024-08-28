from django.db import models

from authentication.models import User

from .helpers.models import TrackingModel


# Create your models here.
class Todo(TrackingModel):  # Inheriting from TrackingModel
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    owner = models.ForeignKey(
        to=User, on_delete=models.CASCADE
    )  # Making a foreign key so each todo can be associated with a user

    def __str__(self):
        return self.title
