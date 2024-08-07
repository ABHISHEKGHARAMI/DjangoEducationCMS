from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
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
    
    
# adding the polymorphoric  content
class Content(models.Model):
    module = models.ForeignKey(Module,
                               related_name='contents',
                               on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type','object_id')
    
    
class ItemBase(models.Model):
    owner = models.ForeignKey(User,
                              related_name='%(class)s_related',
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.title
    
# multi table model inheritance
class Text(ItemBase):
    content = models.TextField()
    
# multi table model inheritance for the File
class File(ItemBase):
    content = models.FileField(upload_to='files')
    
# multi table model inheritance for the image
class Image(ItemBase):
    content = models.FileField(upload_to='images')
    
    
# multi table model inheritance for video
class Video(ItemBase):
    url = models.URLField()
    
    

    
    
    