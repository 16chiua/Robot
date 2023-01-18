from machine import Pin, PWM
from time import sleep

motors =[PWM(Pin(0)), PWM(Pin(1))]
motors[0].freq(50)
motors[1].freq(50)

def start(motorNumber):
    motors[motorNumber].duty_u16(976)
    
def stop(motorNumber):
    motors[motorNumber].duty_u16(0)




start(0)
sleep(1)
stop(0)
