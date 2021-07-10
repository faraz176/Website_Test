from django.db import models

class blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    url = models.URLField(blank=True)
    date = models.DateField()


    def __str__(self):
        return self.title