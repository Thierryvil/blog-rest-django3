from django.db import models


class Publication(models.Model):
    class Meta:
        verbose_name_plural = 'publications'
        db_table = 'publications'

    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    author_id = models.ForeignKey('authors.author', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)
