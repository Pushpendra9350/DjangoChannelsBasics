### Websockets with Django Channels
Here we have made a simple counter app with webscokets.
Websockets implemented in django and consumed by javaScript

#### Configurations
Install
NOTE: Use the same version mentioned here
```git
pip install channels==3.0.4
```

In settings.py 
```py
INSTALLED_APPS = [
    'channels',
    ...
]

#WSGI_APPLICATION = 'ChannelBasics.wsgi.application'
ASGI_APPLICATION = 'ChannelBasics.asgi.application
```
In asgi.py
```py
from channels.routing import ProtocolTypeRouter, URLRouter
from StartApp import routing

...

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(routing.ws_urlpatterns)
})      
```
- **ProtocolTypeRouter**: Will route requests according to there protocol type.

 
