from twisted.internet import protocol,reactor

HOST = '127.0.0.1'
PORT = 21567

class TSCIntProtocol(protocol.Protocol):
 def sendData(self):
   data=raw_input('> ')
   if data:
    self.transport.write(data)
   else:
    self.transport.loseConnection()
 
 def connectionMade(self):
        self.sendData()

 def dataReceived(self, data):
        print data
        self.sendData()

class TSIntFactory(protocol.ClientFactory):
 protocol=TSCIntProtocol
 clientConnectionLost = clientConnectionFailed =\
lambda self,connector,reason:reactor.stop()

reactor.connectTCP(HOST,PORT,TSIntFactory())
reactor.run()
