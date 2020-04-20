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

class ShowManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title must be at least 2 characters"
        if len(postData['network']) < 3:
            errors['network'] = "Network must be at least 3 characters"
        if len(postData['desc']) < 10 and len(postData['desc']) > 0:
            errors['desc'] = "Description is optional, but must be at least 10 characters if used"
        
        

        return errors