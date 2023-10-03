# Importing needed functions
from gpiozero import LED, Buzzer
import subprocess   # ping functions
import time         # sleep function
import datetime     # used for buzzer allowed times

# Define variables
buzz_start = datetime.time(8, 0, 0)
buzz_until = datetime.time(21, 0, 0)
dad_address = "10.0.0.40"
mum_address = "10.0.0.41"
dad_previous_state = None
mum_previous_state = None
# iPhone hibernates and goes on/off erratically so need to bracket it, can't use last state being different
iphone_hibernation_max_s = 300
dad_last_seen_t = datetime.datetime.now()
dad_current_led_colour = "red"

# Define the GPIO pins for LEDs and buzzer
dad_red_led_pin = LED(20)
dad_green_led_pin = LED(21)
mum_red_led_pin = LED(19)
mum_green_led_pin = LED(26)
buzzer_pin = Buzzer(16)

# Function to check if the IP address is reachable
def is_ip_reachable(ip):
    result = subprocess.run(['ping', '-c', '1', ip], capture_output=True)
    return result.returncode == 0


# Function to change the LED color and sound the buzzer
def sound_buzzer():
    if datetime.datetime.now().time() > buzz_start and datetime.datetime.now().time() < buzz_until:
        buzzer_pin.on()
        time.sleep(1)
        buzzer_pin.off()

def dad_led_green():
    dad_red_led_pin.off()
    dad_green_led_pin.on()
    sound_buzzer()

def dad_led_red():
    dad_green_led_pin.off()
    dad_red_led_pin.on()
    sound_buzzer()

def mum_led_green():
    mum_red_led_pin.off()
    mum_green_led_pin.on()
    sound_buzzer()

def mum_led_red():
    mum_green_led_pin.off()
    mum_red_led_pin.on()
    sound_buzzer()

# Set Dad to home to start off
dad_led_red()
# Start looping
while True:
    # Check Dad
    dad_current_state = is_ip_reachable(dad_address)
    if dad_current_state != 0:
        dad_last_seen_t = datetime.datetime.now()
    time_since_dad_last_seen = datetime.datetime.now() - dad_last_seen_t
    seconds_since_dad_last_seen = sum(x * float(t) for x, t in zip([1, 60, 3600], reversed(str(time_since_dad_last_seen).split(":"))))
    print("seconds_since_dad_last_seen: " + str(seconds_since_dad_last_seen))
    print("seconds_since_dad_last_seen > iphone_hibernation_max_s: " + str((seconds_since_dad_last_seen > iphone_hibernation_max_s)))
    if seconds_since_dad_last_seen > iphone_hibernation_max_s and dad_current_led_colour == "red":
        dad_led_green()
        dad_current_led_colour = "green"
    elif seconds_since_dad_last_seen < iphone_hibernation_max_s and dad_current_led_colour == "green":
        dad_led_red()
        dad_current_led_colour = "red"
    #dad_previous_state = dad_current_state

    # Check Mum
    mum_current_state = is_ip_reachable(mum_address)
    if mum_current_state != mum_previous_state:
        if mum_current_state == 0:
            mum_led_green()
        else:
            mum_led_red()
    mum_previous_state = mum_current_state
    time.sleep(2)
