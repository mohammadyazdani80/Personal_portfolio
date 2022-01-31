from django.db import models
from matplotlib.pyplot import title

class Blog (models.Model):
    title = models.CharField(max_length = 100)
    discriptions = models.CharField(max_length = 300,default='' )
    url = models.URLField(blank=True)