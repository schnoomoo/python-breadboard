from signal import pause
from gpiozero import LED


led = LED(26)




for y in range(6,1,-1):
   print (y)
   
   for x in range(5,0,-1):
      print (x, 'little monkeys jumping, 1 fell over, ouch')



led.blink()

pause()



