# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # HTML側から来たURLから、room_nameを変数として取得する
    # この変数名はviews.pyで関数ベースビューで引数として取得できる
    path('<str:room_name>/', views.room, name='room'),
]