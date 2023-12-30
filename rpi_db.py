import sys
import RPi.GPIO as GPIO
import dht11
from time import sleep
import time
import sqlite3


# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()

conn =sqlite3.connect('temperature.db')
c = conn.cursor()

# read data using Pin GPIO17
instance = dht11.DHT11(pin=17)


while True:
    result = instance.read()
    if result.is_valid():
        print("Temp: %d C" % result.temperature +' '+"Humid: %d %%" % result.humidity)
        temperature = result.temperature
        humidity = result.humidity
        date=time.strftime("%Y-%m-%d")
        t=time.strftime("%H:%M:%S")
        c.execute("INSERT INTO dhtsensor(temperature, humidity, Date, Time) VALUES(?,?,?,?)", (temperature, humidity, date, t))
        conn.commit()

    time.sleep(10)
