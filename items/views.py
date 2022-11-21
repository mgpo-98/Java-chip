from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, ItemDetail, ItemPicked
from django.core.paginator import Paginator
from django.db.models import Count
from reviews.models import Review
import csv

# 상품정보를 크롤링해서 model에 저장.


def index(request):
    item = Item.objects.all()
    # csv 파일에서 데이터를 불러온다
    if len(item) == 0:
        items_csv = open("items/items.csv", encoding="UTF-8")
        items_reader = csv.reader(items_csv)
        bulk_list = []
        for i in items_reader:
            bulk_list.append(
                Item(
                    title=i[1],
                    price=i[2],
                    image_url=i[3],
                )
            )
        Item.objects.bulk_create(bulk_list)
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
    # csv 파일에서 데이터를 불러온다
    item_detail_all = ItemDetail.objects.all()
    if len(item_detail_all) == 0:
        item_detail_csv = open("items/item_detail.csv", encoding="UTF-8")
        item_detail_reader = csv.reader(item_detail_csv)
        bulk_list = []
        for i in item_detail_reader:
            bulk_list.append(
                ItemDetail(
                    header_title=i[1],
                    header_image=i[2],
                ),
            )
        ItemDetail.objects.bulk_create(bulk_list)
    review = Review.objects.filter(item_id=item_pk)
    item_detail = ItemDetail.objects.get(pk=item_pk)
    item_info = Item.objects.get(pk=item_pk)
    context = {
        "item_detail": item_detail,
        "item_pk": item_pk,
        "review": review,
        "item_info": item_info,
    }
    return render(request, "items/detail.html", context)


# 담은 상품의 정보를 ItemPicked 테이블에 저장한 후 redirect한다.
def picking(request):
    # picked_items를 itemPicked 테이블에 추가한다
    if request.method == "POST":
        item_info = request.POST.get("item_picked")
        item_smashed = request.POST.get("smashed")
        item_volume = request.POST.get("volume")
        item_amount = request.POST.get("amount")
        picked_items = Item.objects.get(pk=item_info)
        picked_item_list = ItemPicked(
            picked_item=picked_items,
            amount=item_amount,
            smashed=item_smashed,
            volume=item_volume,
        )
        picked_item_list.save()
    return redirect("items:pick")


# 장바구니
def pick(request):
    picked = ItemPicked.objects.all()
    picked_count = picked.aggregate(count=(Count("id")))
    if len(picked) == 0:
        return render(request, "items/pick_none.html")
    else:
        context = {
            "picked": picked,
            "picked_count": picked_count["count"],
            "delivery_fee": 3000,
        }
        return render(request, "items/pick.html", context)


def delete_picked(request):
    print(request.POST)
    return redirect("items:pick")


def before_order(request):
    # 주문금액보기
    # 장바구니 수량 변경
    return redirect("item:pick")


# 검색 기능
# 장바구니 수량 변경, 상품 삭제 구현
