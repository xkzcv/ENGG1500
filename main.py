## NOTE: Minimum & maximum IR read values
# White mins: [2240, 2416, 2320]
# Black maxs: [3712, 3968, 4273]
# Thresholds: [2976, 3192, 3296]
## TODO: dynamic updating as IR reads new values; set new values so mins and maxes are relevant

## NOTE: Various imports
from motor import Motor
import machine
import sys
from ultrasonic import sonic
from time import sleep

## NOTE: Pin setups (IR sensors, motors, ultrasonic sensors)
adc_L = machine.ADC(28)
adc_M = machine.ADC(27)
adc_R = machine.ADC(26)

motor_right = Motor("right", 8, 9, 7)
motor_left = Motor("left", 11,12,13)

ultrasonic_sensor = sonic(17, 16)

while True:
    # NOTE:
    vL = adc_L.read_u16()
    vM = adc_M.read_u16()
    vR = adc_R.read_u16()
    total = vL + vM + vR

    if total == 0:
        error = 0
    else:
        # NOTE: [–1…+1], positive = line is to the left, negative = to the right
        error = (vL - vR) / total
