from mqtt import MQTTClient
from network import WLAN
import pysense
from LIS2HH12 import LIS2HH12 #import accelerometer library
import machine
import time

li = LIS2HH12() #initialise accelerometer

def sub_cb(topic, msg):
    print(msg)

wlan = WLAN(mode=WLAN.STA)
wlan.connect("...ssid...", auth=(WLAN.WPA2, "...wifi password..."), timeout=5000)

print("Connecting to wifi")
while not wlan.isconnected():
    machine.idle()
print("connected to wifi\n")

client = MQTTClient("Pycom", "io.adafruit.com",user="...username...", password="...passord...", port=1883)
client.set_callback(sub_cb)
client.connect()
client.subscribe(topic=<username> + "/feeds/accelerometer-pitch")
client.subscribe(topic=<username> + "/feeds/x-accelerometer")


while True:
    print("roll:", li.roll())
    pitch = str(li.pitch())
    print("pitch:", pitch)
    client.publish(topic=<username> + "/feeds/accelerometer-pitch", msg=pitch)
    time.sleep(3)
    roll = str(li.roll())
    client.publish(topic=<username> + "/feeds/x-accelerometer", msg=roll)
    time.sleep(3)
    if(li.pitch() < 60):
        print("Danger!!!!!!!")
