from django.db import models

from apps.common.models.base_model import BaseModel
from apps.common.models.soft_delete_model import SoftDeleteModel


class BaseAnnouncement(BaseModel, SoftDeleteModel):
    class Meta:
        abstract = True

    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(max_length=1024, blank=False, null=False)
