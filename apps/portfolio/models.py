from django.db import models

# Create your models here.
class Preview(models.Model):
    iconsite    = models.ImageField(upload_to='site_icons/')
    imageofme   = models.ImageField(upload_to='images_of_me/')
    igurl       = models.CharField(max_length=64, null=True, blank=True)
    giturl      = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return f'Portfolio {self.id}'

class Quote(models.Model):
    description = models.TextField(max_length=256, null=True, blank=True)
    image       = models.ImageField(upload_to='quotes/')

    def __str__(self):
        return f'Quote that starts with : {self.description[:10]}'

class Skill(models.Model):
    title       = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField(max_length=256, null=True, blank=True)
    image       = models.FileField(upload_to='skills/')

    def __str__(self):
        return f'{self.title} Skill'

class Project(models.Model):
    title       = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField(max_length=256,null=True, blank=True)
    images      = models.ManyToManyField('ProjectImage' , blank=True)
    techs       = models.ManyToManyField('ProjectTech' , blank=True)
    liveurl     = models.CharField(max_length=64, null=True, blank=True)
    
    def __str__(self):
        return f'{self.title} Project'

class ProjectTech(models.Model):
    tech       = models.CharField(max_length=64, null=True, blank=True)
    
    def __str__(self):
        return f'{self.tech}'

class ProjectImage(models.Model):
    image       = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return f'{self.image}'

class ContactForm(models.Model):
    full_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.full_name
    

class Visit(models.Model):
    ip = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.ip