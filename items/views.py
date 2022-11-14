from django.shortcuts import render
from .crawling import get_items_info, get_item_detail
from .models import Item

# 상품정보를 크롤링해서 model에 저장.


def index(request):
    items = Item.objects.all()
    items_info = get_items_info(1, 9)
    items.image_url = items_info["image_urls"][0]
    context = {
        "image_url": items.image_url,
    }
    return render(request, "items/index.html", context)


def detail(request, item_pk):
    return render(request, "items/detail.html")
