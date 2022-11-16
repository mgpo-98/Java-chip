from django.shortcuts import render, get_object_or_404, redirect
from .crawling import get_items_info, get_item_detail
from .models import Item, ItemDetail, FactSheet, AboutThisCoffee
from django.core.paginator import Paginator

# 상품정보를 크롤링해서 model에 저장.


def index(request):
    item = Item.objects.all()
    # 크롤링한 데이터 데이터테이블에 입력
    # 새로고침을 한 번 해줘야 적용된다.
    if len(item) == 0:
        item_page1 = get_items_info(1, 9)
        item_page2 = get_items_info(2, 9)
        item_page3 = get_items_info(3, 9)
        item_page4 = get_items_info(4, 6)
        for i in range(9):  # 데이터를 가져온다.
            page1 = Item.objects.create(
                title=item_page1["titles"][i],
                image_url=item_page1["image_urls"][i],
                price=item_page1["prices"][i],
            )
        for i in range(9):
            page2 = Item.objects.create(
                title=item_page2["titles"][i],
                image_url=item_page2["image_urls"][i],
                price=item_page2["prices"][i],
            )
        for i in range(9):
            page3 = Item.objects.create(
                title=item_page3["titles"][i],
                image_url=item_page3["image_urls"][i],
                price=item_page3["prices"][i],
            )
        for i in range(6):
            page4 = Item.objects.create(
                title=item_page4["titles"][i],
                image_url=item_page4["image_urls"][i],
                price=item_page4["prices"][i],
            )

    # pagination
    paginator = Paginator(item, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "item": item,
        "page_obj": page_obj,
    }
    return render(request, "items/index.html", context)


def detail(request, item_pk):
    item_detail_object = ItemDetail.objects.all()
    return render(request, "items/detail.html")


# 찜하기(장바구니) : login_required 아님
def pick(request, item_pk):
    # 등록되지 않은 유저의 경우
    # 찜한 아이템이 없는 경우
    # 아이템을 찜한 경우
    return render(request, "items/pick.html")
    if request.method == "POST":
        picked_item = Item.objects.get(pk=item_pk)
        context = {
            "picked_item": picked_item,
        }
        return redirect("item/pick.html")


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
