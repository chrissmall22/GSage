from django.db import models

# Create your models here.

from django.db import models

class Infrastructure(models.Model):
    type = models.CharField(max_length=32)
    url = models.CharField(max_length=256)
    username = models.CharField(max_length=32)
    pw = models.CharField(max_length=32)
    
class Endpoint(models.Model):
    inf = models.ForeignKey(Infrastructure)
    name = models.CharField(max_length=256)
    desc = models.CharField(max_length=256)

class Links(models.Model):
    endpoint_a  = models.CharField(max_length=256)
    endpoint_z  = models.CharField(max_length=256)
    type = models.CharField(max_length=256)
    tag = models.IntegerField(default=0)


