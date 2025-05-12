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

while True:
    sV_all = [sensor.value() for sensor in v_all]
    sys.stdout.write(f"Sensors: {sV_all}.\n")

While