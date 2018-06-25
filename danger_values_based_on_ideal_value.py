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
wlan.connect("...ssid...", auth=(WLAN.WPA2, "...wifi password ... "), timeout=5000)

print("Connecting to wifi")
while not wlan.isconnected():
    machine.idle()
print("connected to wifi\n")

#set up mqtt client
client = MQTTClient("Pycom", "io.adafruit.com",user="..username...", password="...password here ...", port=1883)
client.set_callback(sub_cb)
client.connect()
client.subscribe(topic= username + "/feeds/ideal_posture")



while True:
    pitchString = str(li.pitch())
    client.publish(topic=username + "/feeds/accelerometer-pitch", msg=pitchString)
    print("pitch:", pitchString)


    pitch = li.pitch()
    print("ideal posture",ideal_posture)
    print(li.pitch())
    postureRange = pitch - ideal_posture
    print(postureRange)
    if postureRange > targetRange or postureRange <-targetRange:
        print("Danger!!!!!!!")
        safe = "Danger"
    else:
        safe = "Safe"


    client.publish(topic=username + "/feeds/posture-alert", msg=safe)
    client.check_msg()

    time.sleep(3)
