from gpiozero import LightSensor, LED
from signal import pause

sensor = LightSensor(25)
led = LED(12)

sensor.when_dark = led.on
sensor.when_light = led.off

pause()
