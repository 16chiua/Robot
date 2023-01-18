from machine import Pin, PWM
from time import sleep

def start():
    pwm.duty_u16(976)
    
def stop():
    pwm.duty_u16(0)


pwm = PWM(Pin(1))
pwm.freq(50)

start()
sleep(1)
stop()
