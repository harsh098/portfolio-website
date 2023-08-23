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
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'Resume Dated {str(self.created_at)}'



