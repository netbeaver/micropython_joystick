from machine import Pin
from time import sleep

#0,2,4,5,12,13,14, and 15 all support PWM
L1 = Pin(5, Pin.OUT)
L2 = Pin(4, Pin.OUT)
R1 = Pin(12, Pin.OUT)
R2 = Pin(13, Pin.OUT)

def stop():
    L1.off()
    L2.off()
    R1.off()
    R2.off()

def forward():
    L1.off()
    L2.on()
    R1.off()
    R2.on()

def backward():
    L1.on()
    L2.off()
    R1.on()
    R2.off()

def left(sec=.1):
    L1.on()
    L2.off()
    R1.off()
    R2.on()
    sleep(sec)
    stop()
    
def right(sec=.1):
    L1.off()
    L2.on()
    R1.on()
    R2.off()
    sleep(sec)
    stop()

#stop()