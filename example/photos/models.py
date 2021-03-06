from django.db import models
from cumulus.utils import cumulus_upload_to

class Photo(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=cumulus_upload_to)
    
    def __unicode__(self):
        return self.title