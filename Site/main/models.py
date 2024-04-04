from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class SiteUser(AbstractUser):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class UserInfo(models.Model):
    user = models.ForeignKey(SiteUser, related_name="user", on_delete=models.CASCADE)
    text_info = models.TextField('Description')
    image_info = models.CharField('Image', max_length=1024)

    class Meta:
        verbose_name = 'Info'
        verbose_name_plural = 'Infos'


class Project(models.Model):
    name = models.TextField(verbose_name='name')
    description = models.TextField('Project description')
    image = models.CharField('Image', max_length=1024)

class Education(models.Model):
    name =  models.TextField("Education")
    description = models.TextField("Edu description")
    image = models.CharField('Image', max_length=1024)