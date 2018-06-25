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
client.subscribe(topic="EmmaNiBhriain/feeds/accelerometer-pitch")
client.subscribe(topic="EmmaNiBhriain/feeds/posture-alert")


while True:
    pitch = str(li.pitch())
    client.publish(topic="EmmaNiBhriain/feeds/accelerometer-pitch", msg=pitch)
    print("pitch:", pitch)

    if(li.pitch() < 60):
        print("Danger!!!!!!!")
        safe = "Danger"
    else:
        safe = "Safe"

    client.publish(topic="EmmaNiBhriain/feeds/posture-alert", msg=safe)
    time.sleep(3)
