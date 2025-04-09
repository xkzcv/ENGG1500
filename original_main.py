### !!! PRIORITY !!! DO NOT DELETE ###

from time import sleep
from motor import Motor
from machine import Pin
from ultrasonic import sonic

print("Hello, world!")  # Print a welcome message on reset

line_sensor = Pin(26, Pin.IN)
# Create left and right ‘Motor’ objects
motor_right = Motor("right", 8, 9, 7)
motor_left = Motor("left", 11,12,13)
# These statements make the code more readable.
# Instead of a pin 2 or 3 we can now write "TRIG" or "ECHO"

TRIG = 3
ECHO = 2
ultrasonic_sensor = sonic(TRIG, ECHO)

while True:
    motor_left.set_forwards()  # Set the left motor to run forwards
    motor_right.set_forwards()  # Set the right motor to run forwards
    sensor_value = line_sensor.value()  # Reads 1 if no obstacle is present
    motor_left.duty(sensor_value*50)
    motor_right.duty(sensor_value*50)
    # ...otherwise 0
    # dist = ultrasonic_sensor.distance_mm()
    # if dist <= 100:
    #     motor_speed = 0
    # if dist > 100:
    #     motor_speed = 20
    # motor_left.duty(motor_speed)
    # motor_right.duty(motor_speed)
    # sleep(0.1)
    #



