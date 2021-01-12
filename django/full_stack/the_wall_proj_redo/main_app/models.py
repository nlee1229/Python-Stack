from django.db import models

class UserManager(models.Manager):
    def register_validator(self, post_data):
        errors = {}
        if len(post_data['fname']) < 3:
            errors['fname'] = "First name must be 3 chars or more!"
        if len(post_data['lname']) < 3:
            errors['lname'] = "Last name must be 3 chars or more!"
        if len(post_data['email']) < 8:
            errors['email'] = "Email name must be 8 chars or more!"
        if len(post_data['password']) < 8:
            errors['password'] = "Password name must be 8 chars or more!"
        if post_data['password'] != post_data['confirm_password']:
            errors['confirm'] = "Passwords don't match!"
        return errors

class User(models.Model): 
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    email=models.EmailField()
    password=models.CharField(max_length=255)
    objects=UserManager()

