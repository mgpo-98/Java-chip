from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# 상품정보를 크롤링해서 model에 저장. 상품 정보를 모두 보여준다.


# 목록페이지 정보 크롤링
def get_items_info(page, item_nums):
    items_title_ls = []
    items_image_url_ls = []
    items_price_ls = []
    url = f"https://www.beanbrothers.co.kr/goods/goods_list.php?page={page}&cateCd=001"
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        items = soup.select_one("div.item_basket_type")
        for j in range(1, item_nums + 1):
            items_title = items.select(
                f"ul > li:nth-child({j}) > div > div.item_info_cont > div > div.item_tit_box > a > strong"
            )
            items_image = items.select(
                f" ul > li:nth-child({j}) > div > div.item_photo_box > a > img"
            )
            items_price = items.select(
                "ul > li:nth-child(1) > div > div.item_info_cont > div > div.item_money_box > strong > span"
            )
            items_title_ls.append(items_title[0].get_text())  # 상품명
            items_image_url_ls.append(items_image[0]["src"])  # 상품이미지
            itmes_price_ls.append(items_price[0].get_text())  # 상품 가격
        return {
            "titles": items_title_ls,
            "image_urls": items_image_url_ls,
            "prices": items_price_ls,
        }
    else:
        print(response.status_code)


# 상세페이지 정보 크롤링

# url ='https://www.beanbrothers.co.kr/goods/goods_view.php?goodsNo=1000000216'
# response = requests.get(url)
# if response.status_code == 200:
#     html = response.text
#     soup = BeautifulSoup(html, "html.parser")


def index(request):
    return render(request, "items/index.html")


def detail(request, item_pk):
    return render(request, "items/detail.html")
