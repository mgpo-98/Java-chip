from django.urls import path
from . import views

app_name = "items"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:item_pk>/", views.detail, name="detail"),
    path("pick/<int:item_pk>/", views.pick, name="pick"),  # 임시 경로
    path("test/", views.test, name="test"),
]
