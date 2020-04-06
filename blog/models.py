from django.db import models
from django.urls import reverse
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Contact(models.Model):
    First_Name = models.CharField(max_length = 50)
    Last_Name = models.EmailField(max_length = 50)
    email = models.EmailField(max_length=100)
    message = models.EmailField(max_length = 254)
     
    
    def __str__(self):
        return self.message


   

class Skill(models.Model):
    description = models.CharField(max_length = 300)
    percent = models.IntegerField()
    cv = models.FileField(upload_to='uploads')
    about_me = models.CharField(max_length=100, default=1)
    skills = models.CharField(max_length = 100)
    #percent = models.IntegerField()
    #cv = models.FileField(upload_to='uploads', default=1)

    def __str__(self):
        return self.skills

class Service(models.Model):
    service = models.CharField(max_length = 100)
    s_description = models.CharField(max_length = 300)

    def __str__(self):
        return self.service

class Education(models.Model):
    education = models.CharField(max_length = 100)
    institution = models.CharField(max_length = 100)
    year = models.CharField(max_length = 100)
    s_description = models.CharField(max_length = 300)

    def __str__(self):
        return self.education



class Experience(models.Model):
    experience = models.CharField(max_length = 100)
    company = models.CharField(max_length = 100)
    year = models.CharField(max_length = 100)
    roles = models.CharField(max_length = 200)

    def __str__(self):
        return self.experience


class Project(models.Model):
    project = models.CharField(max_length = 100)
    sub_title = models.CharField(max_length = 100, default=2)
    categories = models.CharField(max_length = 100)
    image = models.FileField(upload_to='images/')
    s_description = models.CharField(max_length = 300)
    technology = models.CharField(max_length = 100)
    image = models.ImageField(default='',
                              blank=True,
                              upload_to='images')
    image_thumbnail = ImageSpecField(source='image',  processors=[ResizeToFill(372, 262)],
                                     format='JPEG',
                                     options={'quality': 60})

    
    
    def __str__(self):
        return self.project
    
    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.pk})


class Review(models.Model):
    review = models.CharField(max_length = 100)
    reviewer = models.CharField(max_length = 100)
    profession = models.CharField(max_length = 100, default=2)
    image = models.ImageField(upload_to='images', default='c-1.png')


    def __str__(self):
        return self.review

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='', blank=True, upload_to='images')
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(372, 262)],
                                     format='JPEG',
                                     options={'quality': 60})
    image_thumbnail2 = ImageSpecField(source='image',
                                      processors=[ResizeToFill(744, 262)],
                                      format='JPEG',
                                      options={'quality': 60})

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
