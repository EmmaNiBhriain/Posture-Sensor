# Posture Sensor
*Posture Sensor* is a project with the aim of improving people's posture. 
The project uses a *Pycom* microcontroller and a *Pysense* expansion board to detect if a person is slouching.
The data is then sent to a dashboard online using WiFi. 


## Components
* Pycom board
* Pysense expansion board
* A USB - micro USB cable
* WiFi connection
* Adafruit account (Free)
* Pycom Battery (optional)
* Atom IDE

## Setup
### Setting up the hardware
There is not a lot of hardware setup required for this project. 
The first step is to connect the Pycom board to the Pysense expansion board. Once they are connected, you simply need to 
power the device. This can be done by connecting the device to your laptop/PC using the USB-micro USB cable.

### Setting up the software
To run the code, you will first need to install Atom if you have not done so already.
Within the IDE, install the Pymakr plugin. This allows you to connect to your Pycom and Pysense board and 
to run code, written within the editor on them.

Next, you need to connect your device to the Pymakr plugin. 
Locate the **settings** option on the Pymakr console and select **global settings**.
A page will open and in the settings there is  field titled Device address. This is where you enter the address of your device.
If you do not know you device address it can be found as follows: 

* Choose the **menu** option on the Pymakr console and select **get serial ports**.
* This prints the available ports connected to your machine.
* Choose the desired port and paste it into the device address field in the settings.

Your device should now be connected to the IDE and you are ready to start writing code!

### Understanding the code
#### Language
The code for this project is written in micropython as this can be run on the Pycom board. 
Therefore, to run scripts you are required to save files as a .py format.

#### Libraries
To use data from the accelerometer in the *Pysense* expansion board in your code, it is necessary to include the LIS2HH12 library.  
Another essential library is the pysense.py library.  
Finally, the mqtt.py library is required as the MQTT protocol is used to communicate with the online dashboard.

#### Accelerometer data
For the purpose of this project, I analysed posture using the pitch values of the accelerometer.  
When the device is positioned upright, the value of the pitch is roughly equal to 90. 
When the device lies horizontally, the value of the pitch is equal to 0.  
By analysing the value of the pitch, it was possible to detect the tilt of the device and therefore, the posture of the person theoretically wearing this device.

##### Accessing the pitch values
1. Import the acclerometer library: `from LIS2HH12 import LIS2HH12`
2. Create an instance of the accelerometer object: `li = LIS2HH12()`
3. Read the pitch values: `pitch = li.pitch()`

#### Using MQTT

1. Import the MQTT library: `from mqtt import MQTTClient`
2. Set up a MQTT client to connect to io.adafruit.com: `client = MQTTClient("device_id", "io.adafruit.com",user="user_name", password="your_password", port=1883)`   
`client.connect()`
##### Publish data
`client.publish(topic="user_name/feeds/feed_name", msg=str(pitch))`  
Note how the pitch value must be converted to a string to be sent to the Adafruit platform. Numerical datatypes are not accepted.

##### Subscribe to a feed
1. Create a callback function to handle incoming data: `def sub_cb(topic, msg):  
    set_posture()  
    print(msg)`  
    `client.set_callback(sub_cb)`
    
2. Subscribe to a feed: `client.subscribe(topic="user_name/feeds/feed_name")`    

#### Connecting to WiFi
1. Import the network library: `from network import WLAN`
2. Configure the WiFi class as a station to allow it to search for existing networks: `wlan = WLAN(mode=WLAN.STA)`
3. Connect to your network: `wlan.connect("ssid", auth=(WLAN.WPA2, "password"), timeout=5000)`
4. Wait for connection to be established: `while not wlan.isconnected():  
    machine.idle()`
