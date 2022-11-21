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
                f"ul > li:nth-child({j}) > div > div.item_info_cont > div > div.item_money_box > strong > span"
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
    item_dict = {
        1: 1000000216,
        2: 1000000215,
        3: 1000000214,
        4: 1000000194,
        5: 1000000170,
        6: 1000000031,
        7: 1000000025,
        8: 1000000026,
        9: 1000000082,
        10: 1000000068,
        11: 1000000188,
        12: 1000000067,
        13: 1000000124,
        14: 1000000032,
        15: 1000000033,
        16: 1000000111,
        17: 1000000034,
        18: 1000000036,
        19: 1000000037,
        20: 1000000222,
        21: 1000000115,
        22: 1000000114,
        23: 1000000065,
        24: 1000000064,
        25: 1000000202,
        26: 1000000113,
        27: 1000000059,
        28: 1000000058,
        29: 1000000056,
        30: 1000000169,
        31: 1000000125,
        32: 1000000112,
        33: 1000000066,
    }
    main_image_url = []
    main_text_h1 = []
    main_text_p = []
    url = f"https://www.beanbrothers.co.kr/goods/goods_view.php?goodsNo={item_dict[goods_number]}"
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
        )["src"]
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
            "header_image": header_item_image,  # header 상품이미지
            "main_images": main_image_url,  # main 상품 이미지들
            "main_text_title": main_text_h1,  # main 제목들
            "main_text_content": main_text_p,  # main 내용들
        }


print("crawling activated")
