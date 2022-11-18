from django.urls import path
from . import views

app_name = "items"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:item_pk>/", views.detail, name="detail"),
    path("pick/", views.pick, name="pick"),  # 임시 경로
    path("picking/", views.picking, name="picking"),
    path("pick/delete", views.delete_picked, name="delete_picked"),
]
