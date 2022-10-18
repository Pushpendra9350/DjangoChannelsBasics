from django.urls import path
from StartApp import consumers

ws_urlpatterns = [
    path("ws/sc/", consumers.MySyncConsumer.as_asgi()),
    path("ws/asc/", consumers.MyASyncConsumer.as_asgi())
]