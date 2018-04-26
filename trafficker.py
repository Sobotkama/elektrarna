#!/usr/bin/python3
from time import sleep
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import threading
import json

def handle(data):
  print()

clients = []

class listener(WebSocket):

  def handleMessage(self):
    self.sendMessage(self.data)
    print(self.data)
    handle(self.data)
  def handleConnected(self):
    print(self.address, 'connected')

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
      testField = {"a":2, "b":"string", "c":True, "d":32.4}
      while True:
          print("runing")
          for client in list(clients):
              msg = json.dumps(testField)
              print(msg)
              client.sendMessage(msg)
          sleep(1)

  t = threading.Thread(target=send_client)
  t.start()


server = SimpleWebSocketServer('', 8000, listener)


print("threadstarted")

server.serveforever()
print("hellllo")

#ws.onmessage = function (evt) 
#               { 
#                  var received_msg = evt.data;
#                  console.log(JSON.parse(received_msg));
#               };
