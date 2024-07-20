from django.db import models

# Create your models here.

class Fileupload(models.Model):
    file=models.FileField(max_length=100)