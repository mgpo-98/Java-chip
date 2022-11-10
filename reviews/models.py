from django.db import models
from django.conf import settings

# 이미지
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

# Datetime
from django.utils import timezone
from datetime import datetime, timedelta


class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    item_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(1200, 960)],
        format="JPEG",
        options={"quality": 95},
    )
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_reviews"
    )
