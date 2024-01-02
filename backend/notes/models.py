from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=70, blank=False, null=False)
    body = models.TextField(default='', blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
