from django.db import models

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=255, blank=False, null=False)
    github = models.URLField(blank=True)
    other_link = models.URLField(blank=True)
    priority = models.IntegerField(default=0)
    image = models.ImageField(upload_to='project_pics', default='blank.png')

    def __str__(self):
        return self.project_name