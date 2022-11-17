from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


class Item(models.Model):
    title = models.CharField(max_length=50)
    price = models.TextField()
    image_url = models.TextField()


# Item detail 모델 추가


class FactSheet(models.Model):
    fieldname = models.TextField()
    content = models.TextField()


class AboutThisCoffee(models.Model):
    title = models.TextField()
    content = models.TextField()


class MainImageUrl(models.Model):
    urls = models.TextField()


class ItemDetail(models.Model):
    fact_sheet = models.ForeignKey(FactSheet, on_delete=models.CASCADE)
    about_this_coffee = models.ForeignKey(AboutThisCoffee, on_delete=models.CASCADE)
    header_title = models.TextField()
    header_image = models.TextField()
    main_images_url = models.ForeignKey(MainImageUrl, on_delete=models.CASCADE)
    main_text_title = models.TextField()
    main_text_content = models.TextField()


# accounts에 ForeiginKey로 연결
class ItemPicked(models.Model):
    picked_item = models.ForeignKey(Item, on_delete=models.CASCADE)
