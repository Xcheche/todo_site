from django.db import models


class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Meta:
    abstract = True
    app_label = "todos" # app label for the model in the database
    ordering = ("-created_at",)
