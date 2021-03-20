import requests
import datetime 
from progress.bar import Bar
from pathlib import Path
import math
import sys
import time

if len(sys.argv) != 3:
    print("Usage:\npython post_fake_data_2.py <datafile> <sensor #>")
    sys.exit(0)

sensor_url= "http://192.168.1.125:8000/api/temperature_sensor/"

BASE_DIR = Path(__file__).resolve().parent

TIME_COLUMN = 1
TEMP_COLUMN = 2
DELIMINATOR = ","
SENSOR = sys.argv[2] 

filename = sys.argv[1] 
with open(BASE_DIR / filename, "r") as data_file:
    bar = Bar('Uploading', max = len(open(BASE_DIR / filename, "r").readlines()) - 1)
    for line in data_file:
        try:
            line_list = line.split(DELIMINATOR)
            epoch = math.floor(float(line_list[TIME_COLUMN]))
            temp = round(float(line_list[TEMP_COLUMN]), 1)
            b = True
            while b:
                #:print(f"{SENSOR} {datetime.datetime.fromtimestamp(epoch)} {temp}")
                r = requests.post(sensor_url, data={
                                        "sensor": SENSOR,
                                        "time": datetime.datetime.fromtimestamp(epoch),
                                        "temperature": temp 
                                        })
                if r.status_code == 201:
                    b = False
                    bar.next()
                else:
                    print(f"{r.status_code} {r.reason}")
                    time.sleep(1)
        except:
            pass

    bar.finish()
