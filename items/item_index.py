# # 크롤링한 데이터 데이터테이블에 입력
#     # 새로고침을 한 번 해줘야 적용된다.
#     if len(item) == 0:
#         item_page1 = get_items_info(1, 9)
#         item_page2 = get_items_info(2, 9)
#         item_page3 = get_items_info(3, 9)
#         item_page4 = get_items_info(4, 6)
#         for i in range(9):  # 데이터를 가져온다.
#             page1 = Item.objects.create(
#                 title=item_page1["titles"][i],
#                 image_url=item_page1["image_urls"][i],
#                 price=item_page1["prices"][i],
#             )
#         for i in range(9):
#             page2 = Item.objects.create(
#                 title=item_page2["titles"][i],
#                 image_url=item_page2["image_urls"][i],
#                 price=item_page2["prices"][i],
#             )
#         for i in range(9):
#             page3 = Item.objects.create(
#                 title=item_page3["titles"][i],
#                 image_url=item_page3["image_urls"][i],
#                 price=item_page3["prices"][i],
#             )
#         for i in range(6):
#             page4 = Item.objects.create(
#                 title=item_page4["titles"][i],
#                 image_url=item_page4["image_urls"][i],
#                 price=item_page4["prices"][i],
#             )
