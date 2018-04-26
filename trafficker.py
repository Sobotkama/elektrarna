from time import sleep
import automationhat
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import threading
import json

def handle(data):
  print(data)

clients = []

class listener(WebSocket):

  def handleMessage(self):
    handle(self.data)

  def handleClose(self):
    print(self.address, 'closed')
  
  def handleConnected(self):
     print(self.address, 'connected')
     clients.append(self)
     for client in clients:
       print("omagawd")
       print("schending masage")
       client.sendMessage(self.address[0] + u' - connected')
  
  
  
  def send_client():
      
      while True:
          testField = automationhat.analog.read()
          for client in list(clients):
              msg = json.dumps(testField)
              client.sendMessage(msg)
          sleep(1)

  t = threading.Thread(target=send_client)
  t.start()


server = SimpleWebSocketServer('', 8000, listener)


print("threadstarted")

server.serveforever()
