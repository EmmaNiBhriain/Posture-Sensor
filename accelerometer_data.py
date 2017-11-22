import pysense
from LIS2HH12 import LIS2HH12
from time import sleep

py = Pysense()
li = LIS2HH12(py)

while True:
    print(li.acceleration())
    print(li.roll())
    print(li.pitch())
sleep(1)
