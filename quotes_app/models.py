from django.db import models
from django.db.models.fields import DateTimeField
from login_app.models import *


class QuoteManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['author']) < 2:
            errors['author'] = "Author must be at least 4 characters"
        if len(postData['quote']) < 2:
            errors['quote'] = "Quote must be at least 10 characters"
        return errors

# Create your models here.
class Quote(models.Model):
    author = models.CharField(max_length=255)
    content = models.TextField()
    added_by = models.ForeignKey(User, related_name = "quotes_added", null = True, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name = "liked_quotes")
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    objects = QuoteManager()