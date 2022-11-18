from django.db import models
from django.conf import settings
from items.models import Item
# 이미지
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

# Datetime
from django.utils import timezone
from datetime import datetime, timedelta


class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order_at = models.DateField('구매일', null=True)
    image = ProcessedImageField(upload_to='images/', blank=True,
                            processors=[ResizeToFill(1200, 960)],
                            format='JPEG',
                            options={'quality': 80})
       
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_reviews"
    )


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
