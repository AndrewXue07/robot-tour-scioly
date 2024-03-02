from machine import Pin, PWM
import time

p5 = Pin(5, Pin.OUT)
p6 = Pin(6, Pin.OUT)
pwm1 = PWM(p5)
pwm2 = PWM(p6)

p18 = Pin(18, Pin.OUT)
p18.on()