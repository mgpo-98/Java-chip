from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


class Item(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    price = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


# Item detail 모델 추가


class FactSheet(models.Model):
    fieldname = models.TextField()
    content = models.TextField()


class AboutThisCoffee(models.Model):
    title = models.TextField()
    content = models.TextField()


class ItemDetail(models.Model):
    fact_sheet = models.ForeignKey(FactSheet, on_delete=models.CASCADE)
    about_this_coffee = models.ForeignKey(AboutThisCoffee, on_delete=models.CASCADE)
    subscribe = models.TextField()
    image = ProcessedImageField(
        upload_to="items/images/",
        blank=True,
        processors=[ResizeToFill(1200, 960)],
        format="JPEG",
        options={"quality": 95},
    )
