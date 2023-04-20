from gpiozero import Button
from signal import pause


button = Button(4)

def button_pressed():
    print("Button was pressed")

def button_held():
   for y in range(6,0,-1):
      print (y)
      for x in range(6,0,-1):
         print (x, 'little monkeys jumping on the bed, 1 fell off and bumped his head, momma called the doctor and the doctor said, no more monkeys jumping on the bed')


def button_released():
    print("Button was released")
    
button.when_pressed = button_pressed
button.when_held = button_held
button.when_released = button_released
 
pause()

'''
for y in range(6,1,-1):
   print (y)
   
   for x in range(5,0,-1):
      print (x, 'little monkeys jumping, 1 fell over, ouch')

'''

from gpiozero import LED

led = LED(26)

led.blink()

pause()
