import struct
from bluepy.btle import DefaultDelegate

class BleDelegate(DefaultDelegate):
    def __init__(self, outerSelf):
        self.outerSelf=outerSelf
        DefaultDelegate.__init__(self)
        print("init delegate called")
    
    def decode(self,data):
        return struct.unpack("f", data)[0]

    def handleNotification(self, cHandle, data):
        value = self.decode(data)
        self.outerSelf.Subject.on_next(value)