from django.db import models


class Author(models.Model):
    class Meta:
        verbose_name_plural = 'authors'
        db_table = 'authors'

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
