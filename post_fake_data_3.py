import requests
import datetime

sensor_url= "http://192.168.1.125:8000/api/temperature_sensor/"

r = requests.post(sensor_url, data = {"sensor": 1,
"time": datetime.datetime(2020,1,1,1,1,1,0),
"temperature": 50})

print(r.status_code)