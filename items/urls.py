from django.urls import path
from . import views

app_name = "items"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:item_pk>/", views.detail, name="detail"),
    path("test/", views.test, name="test"),
]
