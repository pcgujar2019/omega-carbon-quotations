from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField(blank=True)
    contact = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

class Quotation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.RESTRICT)
    reference = models.CharField(max_length=100)
    dated = models.DateField(null=True)
    createddate = models.DateField(null=True)
    salutation = models.CharField(max_length=15)
    subject = models.CharField(max_length=100)
    introduction = models.TextField()
    closing = models.TextField()
    signature = models.CharField(max_length=100)
    termsnconditions = models.TextField()
    status = models.CharField(max_length=50)
  

class Item(models.Model):
    name = models.TextField()
    size = models.CharField(max_length=50, blank=True)
    quantity = models.IntegerField()
    rate = models.FloatField()
    hsncode = models.CharField(max_length=30, blank=True)
    quotation = models.ForeignKey(Quotation, on_delete=models.RESTRICT)
    def __str__(self):
        return self.name