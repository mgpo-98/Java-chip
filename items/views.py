from django.shortcuts import render
from .crawling import get_items_info, get_item_detail
from .models import Item, ItemDetail, FactSheet, AboutThisCoffee

# 상품정보를 크롤링해서 model에 저장.


def index(request):
    item = Item.objects.all()
    if len(item) == 0:
        item_page1 = get_items_info(1, 9)
        for i in range(9):  # 데이터를 가져온다.
            page1 = Item.objects.create(
                title=item_page1["titles"][i],
                image_url=item_page1["image_urls"][i],
                price=item_page1["prices"][i],
            )
    context = {
        "item": item,
    }
    return render(request, "items/index.html", context)


def detail(request, item_pk):
    try:
        item_detail = ItemDetail.objects.get(pk=item_pk)
        if item_detail is None:
            detail_page1 = get_item_detail(1000000216)
            fact_sheet = FactSheet.objects.create(
                fieldname=1,
                content=1,
            )
            about_this_coffee = AboutThisCoffee.objects.create(
                title=1,
                content=1,
            )
            detail1 = ItemDetail.objects.create(
                header_title=detail_page1["header_title"],
                header_image=detail_page1["header_image"],
                main_images_url=detail_page1["main_images"],
                main_text_title=detail_page1["main_text_title"],
                main_text_content=detail_page1["main_text_content"],
                fact_sheet=fact_sheet,
                about_this_coffee=about_this_coffee,
            )
    except ItemDetail.DoesNotExist:
        item_detail = None
    context = {
        "detail1": item_detail,
    }
    return render(request, "items/detail.html", context)


def test(request):
    item = Item.objects.all()
    if len(item) == 0:
        item_page1 = get_items_info(1, 9)
        for i in range(9):
            page1 = Item.objects.create(
                title=item_page1["titles"][i],
                image_url=item_page1["image_urls"][i],
                price=item_page1["prices"][i],
            )
    context = {
        "item": item,
    }
    return render(request, "items/test.html", context)


# 조회수 순 정렬 버튼
# 검색 기능
