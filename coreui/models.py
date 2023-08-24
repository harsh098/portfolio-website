from django.db import models

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=255, blank=False, null=False, verbose_name="Project")
    github = models.URLField(blank=True, verbose_name="Github Link")
    other_link = models.URLField(blank=True, verbose_name="Any Other Link")
    priority = models.IntegerField(default=0, verbose_name="Priority")
    image = models.ImageField(upload_to='project_pics', default='blank.png', verbose_name="Image")

    def __str__(self):
        return self.project_name

class CV(models.Model):
    cv = models.FileField(upload_to='cv')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    def __str__(self):
        return f'Resume Dated {str(self.created_at)}'

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    replied = models.BooleanField(default=False)

    def __str__(self):
        return self.subject

class ContactInfo(models.Model):
    github = models.URLField(default='https://github.com/harsh098')
    linkedin = models.URLField(default='https://www.linkedin.com/in/harsh-mishra-b94096144/')
    twitter = models.URLField(default="https://twitter.com/harsh_dev8086")
    facebook = models.URLField(default=None, null=True, blank=True)
    discord = models.URLField(default='https://discordapp.com/users/776760813469958174')
    instagram = models.URLField(default='https://instagram.com/harsh.dev8086')
    location = models.CharField(default='Noida, India', max_length=255)
    email = models.EmailField(default='hmisraji07@gmail.com')
    youtube = models.URLField(default=None, null=True, blank=True)
    
    def __str__(self):
        return "Social"

class Experience(models.Model):
    date_start = models.DateField(blank=False, null=False)
    date_end = models.DateField(blank=True, null=True, default=None)
    post = models.CharField(max_length=60, null=False, blank=False)
    company = models.CharField(max_length=60, null=False, blank=False)
    ispresent = models.BooleanField(default=False)
    description = models.TextField(max_length=255)

    def __str__(self):
        return f"{str(self.post)}@{str(self.company)}"
    
    def save(self, *args, **kwargs):
        if self.ispresent:
            self.date_end = None  # Set date_end to None if ispresent is True
        if self.date_end is None:
            self.ispresent = True
        super().save(*args, **kwargs)

class Skill(models.Model):
    name = models.CharField(blank=False, null=False, unique=True, max_length=60)
    def __str__(self):
        return str(self.name)

class Brand(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    headline = models.CharField(max_length=225, blank=False, null=False)
    bio = models.TextField(max_length=1000, blank=False, null=False)
    
    def __str__(self):
        return "Brand Information"

class AdCard(models.Model):
    statistic = models.IntegerField(blank=False, null=False)
    claim = models.CharField(blank=False, null=False, max_length=50)

    def __str__(self):
        return "Statistic Cards"


