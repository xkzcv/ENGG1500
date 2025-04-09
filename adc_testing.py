### Can follow a line:
### Will orient left or right, and drive forward


import time
from time import sleep
from motor import Motor
import machine
import sys
import ultrasonic

print("Hello, world!")  # Print a welcome message on reset

adc_L = machine.ADC(28)
adc_M = machine.ADC(27)
adc_R = machine.ADC(26)

motor_right = Motor("right", 8, 9, 7)
motor_left = Motor("left", 11,12,13)

# def forward():
#     motor_left.set_forwards()
#     motor_right.set_forwards()
#     motor_left.duty(40)
#     motor_right.duty(40)
#
# def backward():
#     motor_left.set_backwards()
#     motor_right.set_backwards()
#     motor_left.duty(40)
#     motor_right.duty(40)
#
# def left():
#     motor_left.set_backwards()
#     motor_right.set_forwards()
#     motor_left.duty(40)
#     motor_right.duty(40)
#
# def right():
#     motor_left.set_forwards()
#     motor_right.set_backwards()
#     motor_left.duty(40)
#     motor_right.duty(40)

while True:
    dist = ultrasonic_sensor.distance_mm()
    if dist < 200:
    # The code within this if-statement only gets executed
    # if the distance measured is less than 200 mm
    sys.stdout.write("Distance␣=␣{:6.2f}␣[mm]".format(dist))
    sleep(0.1)

    value_L = adc_L.read_u16()
    value_M = adc_M.read_u16()
    value_R = adc_R.read_u16()

    line_orient = ((value_L*15)+(value_M*0)+(value_R*-15))/(value_L+value_M+value_R) # Weighted Arithmetic Mean (lab 4, page 8; I'm not explaining it) -KJ
    sys.stdout.write(f"{line_orient}mm  from centre.\n") #DEBUG FUNC. -KJ

    motor_left.set_forwards()
    motor_right.set_forwards()
    motor_left.duty(50)
    motor_right.duty(50)

    # while line_orient < 0.6:
    #     forward()
    #     break
    #
    # while line_orient > 0.6: # Read as: if line is to the left, turn left.
    #     left()
    #     break
    #
    # while line_orient > -0.6: # Read as: if line is to the right, turn right.
    #     right()
    #     break


