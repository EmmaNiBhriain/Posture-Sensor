import pysense
from LIS2HH12 import LIS2HH12
from time import sleep

#py = Pysense()
li = LIS2HH12()

while True:
    x = li.acceleration().x
    print(li.acceleration())
    print(x.)
sleep(1)
