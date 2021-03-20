import requests
import datetime 
import random
from progress.bar import Bar


NUM_SQUARES = 40
NUM_DATA_POINTS_PER_BLOCK = 60
unit_url = "http://192.168.1.125:8000/api/sensor_unit/"
sensor_url= "http://192.168.1.125:8000/api/temperature_sensor/"


bar = Bar('Processing', max = NUM_SQUARES*NUM_DATA_POINTS_PER_BLOCK)

for i in range(1, NUM_SQUARES+1):
    a = True
    while a:
        r = requests.post(unit_url, data={"latitude": 0,"longitude": 0 })
        if r.status_code == 201:
            a = False
        else:
            print(r.status_code)
    for j in range(0, NUM_DATA_POINTS_PER_BLOCK):
        b = True
        while b:
            r = requests.post(sensor_url, data={
                                    "sensor": i,
                                    "time": datetime.datetime(2021,3,1,21,42,50,0) + datetime.timedelta(0,j),
                                    "temperature": random.randint(1,100)
                                    })
            if r.status_code == 201:
                bar.next()
                b = False
            else:
                print(r.status_code)

bar.finish()
    
