from django.db import models
from django.utils import timezone

class WishData(models.Model):
    name=models.CharField(max_length=30)
    wishDatetobuy=models.DateField(max_length=20, null=True, blank=True)
    wishobj=models.CharField(max_length=500)
    time = models.DateTimeField()
