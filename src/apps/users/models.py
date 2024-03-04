from django.db import models

from apps.common.models.base_model import BaseModel
from apps.common.models.soft_delete_model import SoftDeleteModel


class User(BaseModel, SoftDeleteModel):
    pass
