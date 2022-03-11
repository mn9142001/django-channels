from django.urls import path

from .consumers import NormalChatConsumer

websocket_urlpatterns = [
    path('<str:partner>/', NormalChatConsumer.as_asgi()),
]
