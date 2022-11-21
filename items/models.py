from django.db import models
from django.conf import settings


class Item(models.Model):
    title = models.CharField(max_length=50)
    price = models.TextField()
    image_url = models.TextField()


# Item detail 모델 추가


class ItemDetail(models.Model):
    header_title = models.TextField()
    header_image = models.TextField()
    # 다음 필드들은 사용하지 않음
    # main_images_url01 = models.TextField()
    # main_images_url02 = models.TextField()
    # main_images_url03 = models.TextField()


# accounts에 ForeiginKey로 연결
class ItemPicked(models.Model):
    picked_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    smashed = models.TextField()
    volume = models.TextField()
    amount = models.IntegerField()


class FactSheet(models.Model):
    fieldname = models.TextField()
    content = models.TextField()


class AboutThisCoffee(models.Model):
    title = models.TextField()
    content = models.TextField()
