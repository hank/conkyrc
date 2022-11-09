from ambient_keys import *
from ambient_api.ambientapi import AmbientAPI
import logging
import time

api = AmbientAPI(AMBIENT_ENDPOINT=AMBIENT_ENDPOINT,
                 AMBIENT_API_KEY=AMBIENT_API_KEY,
                 AMBIENT_APPLICATION_KEY=AMBIENT_APPLICATION_KEY)

devs = api.get_devices()
if len(devs) < 1:
    logging.error('Not enough devices')
    sys.exit(2)

dev = devs.pop()
time.sleep(1)
d = dev.get_data(limit=1)

if len(d) < 1:
    logging.error('Not enough data')
    sys.exit(3)

d = d.pop()
#[{'baromabsin': 27.227,
#  'baromrelin': 29.926,
#  'batt2': 1,
#  'batt3': 1,
#  'batt4': 1,
#  'batt_co2': 1,
#  'battin': 1,
#  'battout': 1,
#  'dailyrainin': 0,
#  'date': '2022-11-09T08:20:00.000Z',
#  'dateutc': 1667982000000,
#  'dewPoint': 14.61,
#  'dewPoint2': 37.7,
#  'dewPoint3': 41.2,
#  'dewPoint4': 22.6,
#  'dewPointin': 39,
#  'eventrainin': 0,
#  'feelsLike': 18.9,
#  'feelsLike2': 63.1,
#  'feelsLike3': 79.7,
#  'feelsLike4': 31.6,
#  'feelsLikein': 67.6,
#  'hourlyrainin': 0,
#  'humidity': 83,
#  'humidity2': 39,
#  'humidity3': 24,
#  'humidity4': 69,
#  'humidityin': 35,
#  'lastRain': '2022-11-06T18:58:00.000Z',
#  'maxdailygust': 8.1,
#  'monthlyrainin': 4.476,
#  'solarradiation': 0,
#  'temp2f': 63.1,
#  'temp3f': 81.5,
#  'temp4f': 31.6,
#  'tempf': 18.9,
#  'tempinf': 67.6,
#  'uv': 0,
#  'weeklyrainin': 0.008,
#  'winddir': 89,
#  'winddir_avg10m': 127,
#  'windgustmph': 3.4,
#  'windspdmph_avg10m': 0.9,
#  'windspeedmph': 2.9,
#  'yearlyrainin': 20.559}]

print(f"Temperature: {d['tempf']}°F")
print(f"Main Floor: {d['tempinf']}°F")
print(f"Basement: {d['temp3f']}°F")
print(f"Upstairs: {d['temp2f']}°F")
print(f"Root Cellar: {d['temp4f']}°F")
print(f"Wind Speed: {d['windspdmph_avg10m']} MPH")
print(f"Wind Gust: {d['windgustmph']} MPH")

