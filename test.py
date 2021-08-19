# test py installations

from gpiorzero import MotionSensor, LED
from signal import pause

pir = MotionSenor(4)
led = LED(16)

pir.when_motion = led.on
pir.when_no_motion = led.off

pause() 
 