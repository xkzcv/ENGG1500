### Can follow a line:
### Will orient left or right, and drive forward


from motor import Motor
import machine
import sys
from ultrasonic import sonic
from time import sleep

adc_L = machine.ADC(28)
adc_M = machine.ADC(27)
adc_R = machine.ADC(26)

motor_right = Motor("right", 8, 9, 7)
motor_left = Motor("left", 11,12,13)

ultrasonic_sensor = sonic(17, 16)

while True:

    value_L = adc_L.read_u16()
    value_M = adc_M.read_u16()
    value_R = adc_R.read_u16()

    try:
        line_pos = ((value_L*10) + (value_M*0) + (value_R*-10)) / (value_L + value_M + value_R) # Weighted Arithmetic Mean (lab 4, page 8; I'm not explaining it) -KJ
    except ZeroDivisionError:
        line_pos = 0

    # sys.stdout.write(f"{line_orient}mm  from centre.\n") #DEBUG FUNC. -KJ

    dist = ultrasonic_sensor.distance_mm()

    if dist <= 200:
        motor_left.duty(0)
        motor_right.duty(0)
        sys.stdout.write("Obstacle detected. Stopping.\n")
        continue

    thresholds = {0: [motor_left.set_forwards(), motor_right.set_forwards(), motor_left.duty(40), motor_right.duty(40)],
                  1: [motor_left.set_forwards(), motor_right.set_forwards(), motor_left.duty(20), motor_right.duty(40)],
                  -1: [motor_left.set_forwards(), motor_right.set_forwards(), motor_left.duty(40), motor_right.duty(20)]}


