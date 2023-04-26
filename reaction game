# Import functions
from gpiozero import Button, LED
from time import sleep, perf_counter_ns
import random

# Define variables to GPIO
led = LED(16)
player_1 = Button(21)
player_2 = Button(20)

# Inital setup
led.off()
time = random.uniform(3, 10)

# Winner variables
p1winner = False
p2winner = False

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
		print("Player 2 pressed too early!!")
		exit()

# Define some variables for losers timeout check
p1extratimemax = float(1)
p1extratime_currently = float(0)
p2extratimemax = float(1)
p2extratime_currently = float(0)
extratimeincrement = 0.001

# OK - goooooooooooo!!!
led.on()
start = perf_counter_ns()

# Check for button presses (or timeout if they are too sloooooowwww)
while True:
    if player_1.is_pressed:
        print("Player 1 wins!")
        p1winner = True
        stop1 = perf_counter_ns()
        led.off()
        # Give player2 a second to press
        while p2extratime_currently <= p2extratimemax:
            p2extratime_currently = p2extratime_currently + extratimeincrement
            sleep(extratimeincrement)
            if player_2.is_pressed:
                # player2 finally pressed (but has already lost)
                stop2 = perf_counter_ns()
                break
        break
    if player_2.is_pressed:
        print("Player 2 wins!")
        p2winner = True
        stop2 = perf_counter_ns()
        led.off()
        # Give player1 a second to press
        while p1extratime_currently <= p1extratimemax:
            p1extratime_currently = p1extratime_currently + extratimeincrement
            sleep(extratimeincrement)
            if player_1.is_pressed:
                # player1 finally pressed (but has already lost)
                stop1 = perf_counter_ns()
                break
        break

# final calculations
if p1extratime_currently >= 0.999:
    t1 = "utter sloth"
else:
     t1 = str(int((stop1-start)/1000000)) + " ms"
if p2extratime_currently >= 0.999:
    t2 = "utter sloth"
else:
     t2 = str(int((stop2-start)/1000000)) + " ms"

# Output result
print("Player 1: " + t1 + "  -  Player2: " + t2)
