from django.utils import timezone
from django.db import models

# Create your models here.
class Farzi(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='farzis/')
    date_added = models.DateTimeField(default=timezone.now) # type: ignore