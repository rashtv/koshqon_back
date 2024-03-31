from django.db import models


class Nationality(models.Model):
    class Meta:
        verbose_name = 'Национальность'
        verbose_name_plural = 'Национальности'
        ordering = ('name', )

    objects = models.Manager()

    name = models.CharField(
        verbose_name='Национальность',
        max_length=128,
    )

    def __str__(self):
        return self.name
