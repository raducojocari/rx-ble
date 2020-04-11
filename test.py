from bluepy.btle import Scanner, DefaultDelegate, Peripheral
import struct

class MyDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
        print("init delegate called")

    def handleNotification(self, cHandle, data):
        print("notification cHandle={}; data={}".format(cHandle, data))

p = Peripheral( "fa:2d:c9:45:90:8e" )
p.withDelegate( MyDelegate() )

# Setup to turn notifications on, e.g.
services=p.getServices()
svc = p.getServiceByUUID("691263ec-5983-4034-8eea-399c82e7fa7a")
ch = svc.getCharacteristics("54fd1583-b8ca-4153-a72f-92d846b041bc")[0]
ch.write(bytes("0", 'utf-8'))

# Main loop --------

while True:
    data = ch.read()
    data2 = struct.unpack("f", data)
    print("{:.2f}".format(data2[0]))
    # Perhaps do something else here

# peripheral = Peripheral("fa:2d:c9:45:90:8e")
# print("mac: {}, addr_type: {}, iface: {}".format(peripheral.addr, peripheral.addrType, peripheral.iface))
# services = peripheral.getServices()
# peripheral.disconnect()
# print("Done")