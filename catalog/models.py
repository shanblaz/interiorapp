from django.db import models

# Create your models here.
import uuid # Required for unique book instances

from django.db import models



class kitchen(models.Model):
   name = models.CharField(max_length = 50)
   picture = models.ImageField(upload_to = 'pictures/kitchen')

   class Meta:
      db_table = "kitchen"
class bedroom(models.Model):
    name = models.CharField(max_length = 50)
    picture = models.ImageField(upload_to = 'pictures/bedroom')

    class Meta:
        db_table = "bedroom"
