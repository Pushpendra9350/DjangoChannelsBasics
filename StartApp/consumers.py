from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio, json
class MySyncConsumer(SyncConsumer):

    # This handler/method is called when client initially opens a connection and it about to finish the handshaking.
    def websocket_connect(self, event):
        print("Websocket connect...", event)
        # With this line it will accept the connection request 
        self.send({'type':'websocket.accept'})
    
    # This handler is called  when data received from client 
    def websocket_receive(self, event):
        print("Websocket message received...", event)
        for i in range(10):
            self.send({
                "type":'websocket.send',
                "text":json.dumps({"count":i})
            })
            sleep(1)

    # This handler is called when either connection to the client is lost either from the client or from server side.
    def websocket_disconnect(self, event):
        print("Websokcet disconneted...", event)
        # Websokcet disconneted... {'type': 'websocket.disconnect', 'code': None} Application instance <Task pending 
        # name='Task-1' coro=<StaticFilesWrapper.__call__() running at /Users/pushpendra/WebDev/channels/venv/lib/python3.9/site-packages/channels/staticfiles.py:44> 
        # wait_for=<Future pending cb=[<TaskWakeupMethWrapper object at 0x1083fe6a0>()]>> for connection <WebSocketProtocol client=['127.0.0.1', 53973] path=b'/ws/sc/'> 
        # took too long to shut down and was killed.
        # FOR THIS ERROR WE NEED TO DO THIS
        raise StopConsumer

class MyASyncConsumer(AsyncConsumer):

    # This handler/method is called when client initially opens a connection and it about to finish the handshaking.
    async def websocket_connect(self, event):
        print("Websocket connect...", event)
        # With this line it will accept the connection request 
        await self.send({'type':'websocket.accept'})
    
    # This handler is called  when data received from client 
    async def websocket_receive(self, event):
        print("Websocket message received...", event)
        for i in range(10):
            await self.send({
                "type":'websocket.send',
                "text":json.dumps({"count":i})
            })
            await asyncio.sleep(1)

    # This handler is called when either connection to the client is lost either from the client or from server side.
    async def websocket_disconnect(self, event):
        print("Websokcet disconneted...", event)
        raise StopConsumer
