from django.shortcuts import render, get_object_or_404, redirect
from .crawling import get_items_info, get_item_detail
from .models import Item, ItemDetail, FactSheet, AboutThisCoffee, ItemPicked
from django.core.paginator import Paginator
from django.db.models import Count

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
    ordered_item = Item.objects.order_by("pk")
    paginator = Paginator(ordered_item, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "item": item,
        "page_obj": page_obj,
    }
    return render(request, "items/index.html", context)


def detail(request, item_pk):
    item_detail_object = ItemDetail.objects.all()
    context = {
        "item_pk": item_pk,
    }
    return render(request, "items/detail.html", context)


# 담은 상품의 정보를 ItemPicked 테이블에 저장한 후 redirect한다.
def picking(request):
    print(request)
    # picked_items를 itemPicked 테이블에 추가한다
    if request.method == "POST":
        item_info = request.POST.get("item_picked")
        item_smashed = request.POST.get("smashed")
        item_volume = request.POST.get("volume")
        item_amount = request.POST.get("amount")
        picked_items = Item.objects.filter(pk=item_info)
        for i in picked_items:
            picked_item_list = ItemPicked(
                picked_item=i,
                amount=item_amount,
            )
        picked_item_list.save()
    return redirect("items:pick")


# 장바구니
def pick(request):
    # 등록되지 않은 유저의 경우
    # 찜한 아이템이 없는 경우
    # 아이템을 찜한 경우
    picked = ItemPicked.objects.all()
    picked_count = picked.aggregate(count=(Count("id")))
    context = {
        "picked": picked,
        "picked_count": picked_count["count"],
    }
    return render(request, "items/pick.html", context)


def delete_picked(request):
    return redirect("items:pick")


# 조회수 순 정렬 버튼
# 검색 기능

# select에서 데이터 불러오기
# 장바구니 데이터 input 수정
# 크롤링코드 수정(csv로 불러오도록)
# form modal 추가
# hover 효과 적용
# 상세페이지에 review table 추가
