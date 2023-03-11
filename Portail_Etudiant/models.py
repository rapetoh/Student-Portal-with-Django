from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class CodeInkForm(models.Model):
    nam=models.CharField(max_length=50)
    surnam=models.CharField(max_length=50)
    mail=models.EmailField()
    messag=models.TextField()
    passwor=models.CharField(max_length=30)
    created_at=models.DateTimeField(auto_now_add=True)

class Uuser(AbstractBaseUser):
    nam=models.CharField(max_length=50, unique=True)
    surnam=models.CharField(max_length=50)
    mail=models.EmailField(unique=True)
    messag=models.TextField()
    passwor=models.CharField(max_length=30)
    created_at=models.DateTimeField(auto_now_add=True)

CATEGORY_CHOICES=[
    ('ALGORITHMIcs','AL'),
    ('MATHS','MA'),
    ('NETWORK','RE'),
    ('PERSONNAL DEVELOPPEMENT','DP'),
]
class cours(models.Model):
    description=models.CharField(max_length=200,default='nothing')
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=40)
    image=models.ImageField(upload_to='course',default='pexels-karolina-grabowska-6256241_dRPoLSw.jpg')


class Lesson(models.Model):
    course = models.ForeignKey(cours, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    fichier = models.FileField(upload_to='documents/')
