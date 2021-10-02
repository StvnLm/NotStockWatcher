from django.db import models

# Create your models here.

class Stock(models.Model):
    ticker = models.TextField(blank=True, null=True)
    asset_description = models.TextField(blank=True, null=True)
    asset_type = models.TextField(blank=True, null=True)
    amount = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    transaction_date = models.DateField(blank=True, null=True)
    senator = models.TextField(blank=True, null=True)