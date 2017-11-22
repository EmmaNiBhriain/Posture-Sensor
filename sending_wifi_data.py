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
wlan.connect("IoT2", auth=(WLAN.WPA2, "ilikecake"), timeout=5000)

print("Connecting to wifi")
while not wlan.isconnected():
    machine.idle()
print("connected to wifi\n")

client = MQTTClient("Pycom", "io.adafruit.com",user="EmmaNiBhriain", password="e99caf87d89749f28926c88d7170137c", port=1883)
client.set_callback(sub_cb)
client.connect()
client.subscribe(topic="EmmaNiBhriain/feeds/x-accelerometer")

while True:
    #print(li.roll())
    roll = str(li.roll())
    client.publish(topic="EmmaNiBhriain/feeds/x-accelerometer", msg=roll)
    time.sleep(3)
    roll = str(li.roll())
    client.publish(topic="EmmaNiBhriain/feeds/x-accelerometer", msg=roll)
    time.sleep(3)
