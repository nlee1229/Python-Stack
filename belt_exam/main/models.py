from django.db import models
from django.db.models.fields.related import ForeignKey
from login_reg.models import User

class TripManager(models.Manager):
    
    def validator(self, postData):
        errors = {}
        if len(postData['destination']) < 2:
            errors['destination'] = " Destination should be at least 2 characters."
        if len(postData['start_date']) < 3:
            errors['start_date'] = "Start date should be at least 3 characters."
        if len(postData['end_date']) < 10:
            errors['end_date'] = "End date should be at least 10 characters."
        if len(postData['content']) < 10:
            errors['content'] = "Plan should be at least 10 characters."      
        return errors


class Trip(models.Model):
    destination = models.CharField(max_length = 255)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    content = models.TextField()
    by_user =  models.ForeignKey(User, related_name="byusers", on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripManager()


