from django.db import models


class SoftDeleteModel(models.Model):
    class Meta:
        abstract = True

    is_deleted = models.BooleanField(default=False)

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()
