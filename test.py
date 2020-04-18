from BleReader import BleReader
from InfluxClient import InfluxClient




influx = InfluxClient(
            url="http://192.168.1.23:9999", 
            token="DDHT0emN0wa00JZSxgo3b5ji_pbAbmnjVZj_F5py1UhJYam63KaRr68oU_1vopla1H62vVNiA86kh7i3ln1Spg==")

reader = BleReader(
            peripheralAddress="fa:2d:c9:45:90:8e", 
            serviceUUID="691263ec-5983-4034-8eea-399c82e7fa7a", 
            charUUID="54fd1583-b8ca-4153-a72f-92d846b041bc")

obs = reader.connect()
obs.subscribe(
    on_next= lambda i: print("data={}".format(i)),
    on_error= lambda e: print("Error occured: {}".format(e)),
    on_completed= lambda: print("Done")
)

reader.start()






# # peripheral.disconnect()
# # print("Done")
