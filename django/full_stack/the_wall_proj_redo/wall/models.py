from django.db import models
from django.db.models.fields import related
from main_app.models import User

class PostMessage(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, related_name="postmessages", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    postmessage = models.ForeignKey(PostMessage, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)