from django.db import models


class City(models.Model):
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ('name', )

    objects = models.Manager()

    name = models.CharField(
        verbose_name='Название города',
        max_length=128,
    )
    code = models.CharField(
        verbose_name='Код города',
    )

    def __str__(self):
        return self.name
