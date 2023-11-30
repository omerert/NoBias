from django.db import models

# Create your models here.
class SubmittedLink(models.Model):
    link = models.URLField()