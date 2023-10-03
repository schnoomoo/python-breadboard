from gpiozero import LED
from time import sleep

gpio20 = LED(20)
gpio21 = LED(21)

while True:
    gpio20.on()
    gpio21.off()
    sleep(1)
    gpio20.off()
    gpio21.on()
    sleep(1)
