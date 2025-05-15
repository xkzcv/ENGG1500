### Can follow a line:
### Will orient left or right, and drive forward


from motor import Motor
from machine import Pin
import sys
import time

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
v_all = [V5, V4, V3, V2, V1]

# Movement duration
STEP_TIME = 0.05  # length of step
SLEEP_AFTER_STOP = 0.07  # pause after stopping. 


# State functions
current_state = 'forward'

def forward():
    motor_left.set_forwards()
    motor_right.set_forwards()
    motor_left.duty(40)
    motor_right.duty(40)
    current_state = 'forward'

def sharp_left():
    motor_left.set_backwards()
    motor_right.set_forwards()
    motor_left.duty(40)
    motor_right.duty(40)
    current_state = 'left'

def sharp_right():
    motor_left.set_forwards()
    motor_right.set_backwards()
    motor_left.duty(40)
    motor_right.duty(40)
    current_state = 'right'

def smooth_left():
    motor_left.set_forwards()
    motor_right.set_forwards()
    motor_left.duty(30)
    motor_right.duty(40)
    current_state = 'left'

def smooth_right():
    motor_left.set_forwards()
    motor_right.set_forwards()
    motor_left.duty(40)
    motor_right.duty(30)
    current_state = 'right'

def reverse():
    motor_left.set_backwards()
    motor_right.set_backwards()
    motor_left.duty(40)
    motor_right.duty(40)

def searching():
    if current_state == 'left':
        sharp_left()
    elif current_state ==  'right':
        sharp_right()
    elif current_state == 'forward':
        reverse()


def park():
    motor_left.set_forwards()
    motor_right.set_forwards()
    motor_left.duty(0)
    motor_right.duty(0)



# --- Main Loop --- #
while True:
    sV_all = [sensor.value() for sensor in v_all]
    sys.stdout.write(f"Sensors: {sV_all}.\n")
    if sV_all in ([0, 0, 1, 0, 0], [0, 1, 1, 1, 0]):
        forward()
    elif sV_all in ([0, 1, 1, 0, 0], [0, 1, 0, 0, 0]):
        smooth_left()
    elif sV_all in ([1, 1, 0, 0, 0], [1, 0, 0, 0, 0]):
        sharp_left()
    elif sV_all in ([0, 0, 1, 1, 0], [0, 0, 0, 1, 0]):
        smooth_right()
    elif sV_all in ([0, 0, 0, 1, 1], [0, 0, 0, 0, 1]):
        sharp_right()
    else:
        searching()
        
    time.sleep(STEP_TIME)
    park()
    time.sleep(SLEEP_AFTER_STOP)

