# Import functions
from gpiozero import Button, LED
from time import sleep
import random

# Define variables to GPIO
red = LED(24)
green = LED(25)

#test
while True:
	green.off()
	red.on()
	sleep(1)
	red.off()
	green.on()
	sleep(1)

'''
# Inital setup
led.off()
time = random.uniform(3, 10)

#print(time)

# Loop watching for enthusiastic button pushes (instead of sleeping)
y = 0
check_period = 0.1
while y < time:
	y = y + check_period
	sleep(check_period)
#	print(y)
	if player_1.is_pressed:
		print("Player 1 pressed too early!!")
		exit()
	if player_2.is_pressed:
		print("Player 2 pressed too early!!")		exit()

# OK - goooooooooooo!!!	
led.on()

while True:
    if player_1.is_pressed:
        print("Player 1 wins!")
        break
    if player_2.is_pressed:
        print("Player 2 wins!")
        break

led.off()
'''
