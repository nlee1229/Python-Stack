from django.db import models

    
class Movie(models.Model): #movie inherits from models.Model   and models.model is coming from the import models on line 1
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self): #essentially overriding the models to string method
        return "Title: {}".format(self.title)