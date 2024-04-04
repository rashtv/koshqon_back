from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True

    id = models.BigAutoField(
        primary_key=True,
        editable=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
    )
