from django.db import models


# Create your models here.
class addclients(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    ccp = models.IntegerField(max_length=30)
    cle = models.IntegerField(max_length=30)

    def __str__(self):
        return self.name


class Worker(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    worker = models.ForeignKey(
        Worker, on_delete=models.CASCADE, related_name="invoices"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice {self.id} - {self.worker.name}"
