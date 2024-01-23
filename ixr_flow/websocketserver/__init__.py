from websockets.sync.server import serve
import time
from threading import Thread

DEFAULTBIND = "localhost"
DEFAULTPORT = 8350

# clients
clients = set()

class WebSocketServer(Thread):
    def handler(self, websocket):
        # client connected, add to the set
        clients.add(websocket)

        try:
            for message in websocket:
                pass
        except:
            pass
            
    def send(self, message):
        to_remove = []
        for client in clients:
            try:
                client.send(message)
            except:
                to_remove.append(client)
        for client in to_remove:
            clients.remove(client)    

    def run(self):
        with serve(self.handler, host=self.bind, port=self.port) as server:
            server.serve_forever()

    def __init__(self, bind = DEFAULTBIND, port = DEFAULTPORT):
        super().__init__()
        self.bind = bind
        self.port = port