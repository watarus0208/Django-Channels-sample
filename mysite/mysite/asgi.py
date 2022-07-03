"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from pprint import pp

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# プロトコルをマッピングする
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        # ここでscopeが生成される
        URLRouter(
            # URLSolverで設定された値がリストで詰まってる
            # viewのインスタンスも
            chat.routing.websocket_urlpatterns
        )
    ) 
})