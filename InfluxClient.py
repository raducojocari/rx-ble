import influxdb_client


from influxdb_client import InfluxDBClient, Point, WritePrecision

class InfluxClient:
    def __init__(self, url, token):
        client = InfluxDBClient(url=url,token=token)
        self.influx = client.write_api()


    def emitMetric(self, value):
        print("value={:.2f}".format(value))

        point = Point("generated")\
            .tag("host", "host1")\
            .field("value",value)

        self.influx.write("solar", "0587886f264c9000", point)
