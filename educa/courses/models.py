from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# model for the  subject
class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    
    # meta class for the subjects model for the ordering
    class Meta:
        ordering = ['title']
        
    #string method
    def __str__(self):
        return self.title
    
    
# model for the courses
class Course(models.Model):
    owner = models.ForeignKey(User,
                              related_name='corses_created',
                              on_delete=models.CASCADE)
    
    subject = models.ForeignKey(Subject,
                                related_name='courses',
                                on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    overview = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']
        
    def __str__(self):
        return self.title
    
    
# class for the module
class Module(models.Model):
    course = models.ForeignKey(Course,
                               related_name='modules',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    class Meta:
        ordering = ['title']
        
    
    # str method
    def __str__(self):
        return self.title
    
    
    
    