### Can follow a line:
### Will orient left or right, and drive forward


from motor import Motor
from machine import Pin
import sys
from ultrasonic import sonic
from time import sleep

adc_LL = Pin(21, Pin.IN)
adc_L = Pin(20, Pin.IN)
adc_M = Pin(19, Pin.IN)
adc_R = Pin(18, Pin.IN)
adc_RR = Pin(17, Pin.IN)

motor_right = Motor("right", 8, 9, 7)
motor_left = Motor("left", 11,12,13)

ultrasonic_sensor = sonic(17, 16)

while True:

    value_LL = adc_LL.value()
    value_L = adc_L.value()
    value_M = adc_M.value()
    value_R = adc_R.value()
    value_RR = adc_RR.value()

    motor_left.set_forwards()
    motor_right.set_forwards()

    if line_pos == 0:
        motor_left.duty(40)
        motor_right.duty(40)
    elif line_pos == 1:
        motor_left.duty(20)
        motor_right.duty(40)
    elif line_pos == -1:
        motor_left.duty(40)
        motor_right.duty(20)
    else:
        motor_left.duty(0)
        motor_right.duty(0)

    sys.stdout.write(f"Value LL={value_LL:.2f} | Value LL={value_L:.2f} | Value LL={value_M:.2f} | Value LL={value_R:.2f} | Value LL={value_RR:.2f}\n")


