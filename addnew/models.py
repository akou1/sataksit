from django.db import models


# Create your models here.
class addclients(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    ccp = models.IntegerField(max_length=30)
    cle = models.IntegerField(max_length=30)

    def __str__(self):
        return self.name
