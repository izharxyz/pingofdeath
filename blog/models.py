from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

import uuid

class Blog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog')
    title = models.CharField(
        max_length=128,
        validators=[MinLengthValidator(5, 'title must be greater than 5 characters')])
    body = models.TextField(
        validators=[MinLengthValidator(100, 'blog must be greater than 100 characters')]
    )
    image = models.ImageField(upload_to='blog_thumbnails')

    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title