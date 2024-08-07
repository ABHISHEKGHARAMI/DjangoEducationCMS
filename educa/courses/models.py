from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# model for the  subject
class Subject(models.Model):
    title = models.CharField(max_length=200)
    slugfield = models.SlugField(max_length=200,unique=True)
    
    # meta class for the subjects model for the ordering
    class Meta:
        ordering = ['title']
        
    #string method
    def __str__(self):
        return self.title
    