from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    # chatアプリのルーティング
    # as_asgi():各ユーザコネクション毎にASGIインスタンスを作成
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]