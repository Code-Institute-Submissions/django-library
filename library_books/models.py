from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=254, default='')
    author = models.CharField(max_length=254, default='')
    genre = models.CharField(max_length=254, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    checkedOut = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)
    checked_by = models.CharField(max_length=254, default='', blank=True)

    def __str__(self):
        return self.title
        