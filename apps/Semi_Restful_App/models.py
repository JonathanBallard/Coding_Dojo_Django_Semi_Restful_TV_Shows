from django.db import models 
 
# create your models here 
# Field Types Link: https://docs.djangoproject.com/en/1.11/ref/models/fields/#field-types 
 
class Show(models.Model):
    title = models.CharField(max_length = 45)
    network = models.CharField(max_length = 45)
    release_date = models.DateTimeField()
    desc = models.TextField(default="Description...")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
