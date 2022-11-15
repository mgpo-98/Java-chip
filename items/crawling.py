import requests
from bs4 import BeautifulSoup
import asyncio

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
            items_price_ls.append(items_price[0].get_text())  # 상품 가격
        return {
            "titles": items_title_ls,
            "image_urls": items_image_url_ls,
            "prices": items_price_ls,
        }
    else:
        print(response.status_code)


# 상세페이지 정보 크롤링


def get_item_detail(goods_number):
    header_image_url = []
    main_image_url = []
    main_text_h1 = []
    main_text_p = []
    url = f"https://www.beanbrothers.co.kr/goods/goods_view.php?goodsNo={goods_number}"
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        # header
        header_item = soup.select_one("div.item_photo_info_sec")
        header_item_title = header_item.select_one(
            ".item_detail_tit > h3:nth-child(1)"
        ).get_text()
        header_item_image = soup.select_one(
            "div.item_photo_view_box:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > img:nth-child(1)"
        )["src"][0]
        header_image_url.append(header_item_image)

        # main
        main = soup.select_one("div.detail_view:nth-child(1)")
        main_image = main.find_all("img")
        for i in range(len(main_image)):
            main_image_url.append(main_image[i]["src"])
        main_text = main.find_all("div", class_="txt")
        for i in main_text:
            main_text_h1.append(i.find("h1").get_text())
            main_text_p.append(i.find("p").get_text())
        return {
            "header_title": header_item_title,  # header 상품명
            "header_image": header_image_url,  # header 상품이미지
            "main_images": main_image_url,  # main 상품 이미지들
            "main_text_title": main_text_h1,  # main 제목들
            "main_text_content": main_text_p,  # main 내용들
        }


print("activated")
