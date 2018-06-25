from mqtt import MQTTClient
from network import WLAN
import pysense
from LIS2HH12 import LIS2HH12 #import accelerometer library
import machine
import time

##Program to set ideal posture by pressing a button on an adafruit dashboard online

li = LIS2HH12() #initialise accelerometer
global ideal_posture
targetRange = 20

def set_posture():
    global ideal_posture
    ideal_posture=li.pitch()
    print(ideal_posture)

set_posture()  #initialise the ideal_posture

def sub_cb(topic, msg):
    set_posture()
    print(msg)


#Connect to wifi
wlan = WLAN(mode=WLAN.STA)
wlan.connect("IoT2", auth=(WLAN.WPA2, "ilikecake"), timeout=5000)

print("Connecting to wifi")
while not wlan.isconnected():
    machine.idle()
print("connected to wifi\n")

#set up mqtt client
client = MQTTClient("Pycom", "io.adafruit.com",user="EmmaNiBhriain", password="e99caf87d89749f28926c88d7170137c", port=1883)
client.set_callback(sub_cb)
client.connect()
client.subscribe(topic="EmmaNiBhriain/feeds/ideal_posture")


while True:
    pitch = li.pitch()
    print("ideal posture",ideal_posture)
    print(li.pitch())
    postureRange = pitch - ideal_posture
    print(postureRange)
    if postureRange > targetRange or postureRange <-targetRange:
        print("Danger")
    client.check_msg()
    time.sleep(1)
