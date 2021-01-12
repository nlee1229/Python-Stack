from django.db import models

    # class DojoManager(models.Manager):
    #     def register_validator(self, post_data):
    #         errors = {}
    #         if len(post_data['name']) < 1:
    #             errors['name'] = "Name must be 1 chararacter or more!"
    #         if len(post_data['city']) < 3:
    #             errors['city'] = "City must be 3 characters or more!"
    #         if len(post_data['state']) < 3:
    #             errors['state'] = "State name must be 3 characters or more!"
    #         return errors

    # class NinjaManager(models.Manager):
    #     def register_validator(self, post_data):
    #     errors = {}
    #     if len(post_data['fname']) < 3:
    #         errors['fname'] = "Name must be 3 chars or more!"
    #     if len(post_data['lname']) < 3:
    #         errors['lname'] = "Last name must be 3 chars or more!"

    #     return errors

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Ninja(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    dojoid = models.ForeignKey(Dojo, related_name="ninjas", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)