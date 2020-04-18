from rx import create
from rx.subject import Subject

from bluepy.btle import Scanner, Peripheral

from BleDelegate import BleDelegate

class BleReader():
    def __init__(self, peripheralAddress, serviceUUID, charUUID):
        self.peripheralAddress=peripheralAddress
        self.serviceUUID=serviceUUID
        self.charUUID=charUUID

    def enable_notify(self, chara_uuid):
        setup_data = b"\x01\x00"
        notify = self.peripheral.getCharacteristics(uuid=chara_uuid)[0]
        notify_handle = notify.getHandle() + 1
        self.peripheral.writeCharacteristic(notify_handle, setup_data, withResponse=True)
    
    def connect(self):
        self.peripheral = Peripheral(self.peripheralAddress)
        self.peripheral.withDelegate( BleDelegate(self) )
        self.Subject = Subject()

         # Setup to turn notifications on, e.g.
        services=self.peripheral.getServices()
        svc = self.peripheral.getServiceByUUID(self.serviceUUID)
        ch = svc.getCharacteristics(self.charUUID)[0]
        self.enable_notify(self.charUUID)
        return self.Subject

    def start(self):
        while True:
            if self.peripheral.waitForNotifications(0):
                continue
            print("Waiting...")
        #Add error handling