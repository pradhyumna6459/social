from django.db import models
class data(models.Model):

    name = models.CharField(max_length=100)
    cause=models.CharField(max_length=100)
    img =models.ImageField(upload_to='pics')
    size = models.IntegerField()
    desc =models.TextField()
    link=models.CharField(max_length=100)
# Create your models here.
