from pickle import TRUE
from pydoc import describe
from pyexpat import model
from django.db import models
from matplotlib import image
from numpy import imag

class Project(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 250 , default='description')
    image = models.ImageField(upload_to = 'portfolio/image/')
    url = models.URLField(blank = True)
