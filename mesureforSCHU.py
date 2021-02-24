#!/usr/bin/env python3

import serial
import time
import datetime
import json

SERIALPORT= "/dev/serial0"

PACKET = [0xFF, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79]


def sendToInfluxDB(dataasjson):
    host = "YOURIPOFINFLUX"
    port = 8086
    user = 'influxdbuser'
    password = 'YOURPASSWORD'
    dbname = 'forSCHU'

    from influxdb import InfluxDBClient
    client = InfluxDBClient(host, port, user, password, dbname)
    entry = [{'measurement': 'CO2',
              'tags': {'host': 'MHZ14a'},
              'time': dataasjson['dt'],
              'fields': {
                  'PPM': float(dataasjson['ppm'])}
              }]
    ret = client.write_points(entry)
    # print(entry)
    print("write_points() to Influxdb on %s db=%s worked=%s  ppm=%s time=%s" % (host, dbname, str(ret), dataasjson['ppm'], dataasjson['dt']))

def getData(serialconnection):
    serialconnection.write(bytearray(PACKET))
    response = serialconnection.read(size=9)
    response = bytearray(response)
    checksum = 0xff & (~(response[1] + response[2] + response[3] + response[4] + response[5] + response[6] + response[7]) + 1)
    serialconnection.close()

    if response[8] == checksum:
        dt= (datetime.datetime.now(datetime.timezone.utc).isoformat())
        return {
            "ppm": (response[2] << 8) | response[3],
            "dt": dt
           # "ts": datetime.datetime.today().timestamp(),
        }
    else:
        raise Exception("checksum: " + hex(checksum))

def main():
   while True:
       serialconnection = serial.Serial(SERIALPORT, 9600, timeout=1)
       time.sleep(2)

       time.sleep(60)
       dataasjson = getData(serialconnection)
       sendToInfluxDB(dataasjson)

if __name__ == '__main__':
    main()
