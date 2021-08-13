from django.db import models


class Proposal(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='proposal', null=True, blank=True)
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.title
        
# Create your models here.
