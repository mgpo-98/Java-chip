from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.


class Item(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    price = models.IntegerField()
    created_at = models.DatetimeField(Auto_now_add=True)
    image = models.ProcessedImageField(
        upload_to="items/images/",
        blank=True,
        processors=[ResizeToFill(1200, 960)],
        format="JPEG",
        options={"quality": 95},
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    want = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="wanted_item")
