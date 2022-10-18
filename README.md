## Important Notes to setup ASGI Application for Django Channels
1. Install: pip install channels
2. Add channels to installed apps in starting
3. Settings.py > chnage [WSGI_APPLICATION = 'ChannelBasics.wsgi.application' -> ASGI_APPLICATION = 'ChannelBasics.asgi.application']
4. asgi.py > add ProtocolTypeRouter to route correct request to coorect protocol application 
"""py
application = ProtocolTypeRouter({
    "http": get_asgi_application()
})
"""
5. 

