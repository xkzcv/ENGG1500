### Can follow a line:
### Will orient left or right, and drive forward


from motor import Motor
from machine import Pin
import sys

# --- Configuration --- #
# Motor Pins
motor_right = Motor("right", 8, 9, 7)
motor_left = Motor("left", 11,12,13)

# Digital Sensor Pins
V1 = Pin(21, Pin.IN)
V2 = Pin(20, Pin.IN)
V3 = Pin(19, Pin.IN)
V4 = Pin(18, Pin.IN)
V5 = Pin(17, Pin.IN)
v_all = [V1, V2, V3, V4, V5]

def centre():
    motor_left.set_forwards()
    motor_right.set_forwards()
    motor_left.duty(40)
    motor_right.duty(40)

def left():
    motor_left.set_forwards()
    motor_right.set_forwards()
    motor_left.duty(30)
    motor_right.duty(50)

def sharp_left():
    motor_left.set_forwards()
    motor_right.set_forwards()
    motor_left.duty(20)
    motor_right.duty(60)

def right():
    motor_left.set_forwards()
    motor_right.set_forwards()
    motor_left.duty(50)
    motor_right.duty(30)

def sharp_right():
    motor_left.set_forwards()
    motor_right.set_forwards()
    motor_left.duty(60)
    motor_right.duty(20)

while True:
    sV_all = [sensor.value() for sensor in v_all]
    sys.stdout.write(f"Sensors: {sV_all}.\n")
    if sV_all == [0, 0, 1, 0, 0]:
        centre()
    elif sV_all in ([0, 1, 1, 0, 0], [0, 1, 0, 0, 0]):
        left()
    elif sV_all in ([1, 1, 0, 0, 0], [1, 0, 0, 0, 0]):
        sharp_left()
    elif sV_all in ([0, 0, 1, 1, 0], [0, 0, 0, 1, 0]):
        right()
    elif sV_all in ([0, 0, 0, 1, 1], [0, 0, 0, 0, 1]):
        sharp_right()
    else:
        # Lost line — stop or slow down to recover
        motor_left.duty(0)
        motor_right.duty(0)