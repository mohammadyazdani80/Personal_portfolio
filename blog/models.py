from time import time
from django.db import models
from matplotlib.pyplot import title

class Blog (models.Model):
    title = models.CharField(max_length = 100)
    discriptions = models.CharField(max_length = 300,default='' )
    time = models.DateTimeField(auto_now=True)
    url = models.URLField(blank=True)