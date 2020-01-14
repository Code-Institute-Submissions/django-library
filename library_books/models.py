from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=254, default='')
    author = models.CharField(max_length=254, default='')
    genre = models.CharField(max_length=254, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    checkedOut = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)

    """
    def check_in_out(self):

        if self.checkedOut == False:
            self.checkedOut = True
        else:
            self.checkedOut = False
        self.save()
    """

    def __str__(self):
        return self.title
        