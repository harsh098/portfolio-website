from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Project)
admin.site.register(models.CV)
admin.site.register(models.Message)
admin.site.register(models.Experience)
admin.site.register(models.ContactInfo)
admin.site.register(models.Skill)
admin.site.register(models.Brand)
admin.site.register(models.AdCard)