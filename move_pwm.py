from machine import Pin, PWM
from time import sleep

#0,2,4,5,12,13,14, and 15 all support PWM
L1 = Pin(5)
L2 = Pin(4)
R1 = Pin(12)
R2 = Pin(13)

pwm_L1 = PWM(L1)
pwm_L2 = PWM(L2)
pwm_R1 = PWM(R1)
pwm_R2 = PWM(R2)


pwm_L1.freq(100)
pwm_L2.freq(100)
pwm_R1.freq(100)
pwm_R2.freq(100)

#min speed: 350
def stop():
    pwm_L1.duty(0)
    pwm_L2.duty(0)
    pwm_R1.duty(0)
    pwm_R2.duty(0)


def forward(l=512,r=512):
    pwm_L1.duty(0)
    pwm_L2.duty(l)
    pwm_R1.duty(0)
    pwm_R2.duty(r)

def backward(l=512,r=512):
    pwm_L1.duty(l)
    pwm_L2.duty(0)
    pwm_R1.duty(r)
    pwm_R2.duty(0)


stop()


