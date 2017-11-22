from mqtt import MQTTClient
from network import WLAN
import machine
import time

def sub_cb(topic, msg):
    print(msg)

wlan = WLAN(mode=WLAN.STA)
wlan.connect("IoT2", auth=(WLAN.WPA2, "ilikecake"), timeout=5000)

while not wlan.isconnected():
    machine.idle()
print("connected to wifi\n")

client = MQTTClient("COM6", "io.adafruit.com",user="EmmaNiBhriain", password="e99caf87d89749f28926c88d7170137c", port=1883)
client.set_callback(sub_cb)
client.connect()
client.subscribe(topic="EmmaNiBhriain/feeds/x-accelerometer")

while True:
    print("sending value 90")
    client.publish(topic="EmmaNiBhriain/feeds/x-accelerometer", msg="90")
    time.sleep(1)
    print("sending value 20")
    client.publish(topic="EmmaNiBhriain/feeds/x-accelerometer", msg="20")

    time.sleep(1)
