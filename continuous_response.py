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

    line_pos = max(-3, min(3, line_pos))
    base_speed = 37.5

    k = 1.0

    adjust = k * (line_pos / 3)  # Normalize between -1 and 1

    left_speed = base_speed * (1.0 - max(0, adjust))  # Reduce left speed when turning right
    right_speed = base_speed * (1.0 + min(0, adjust))  # Reduce right speed when turning left

    # Clamp speeds to [0, 100]
    left_speed = max(25, min(50, left_speed))
    right_speed = max(25, min(50, right_speed))

    motor_left.set_forwards()
    motor_right.set_forwards()
    motor_left.duty(int(left_speed))
    motor_right.duty(int(right_speed))

    sys.stdout.write(f"LineOrient={line_pos:.2f} | L={left_speed:.1f} R={right_speed:.1f} | Dist={dist:.1f}mm\n")

    sleep(0.5)

    # while line_pos < 0.6:
    #     forward()
    #     break
    #
    # while line_pos > 0.6: # Read as: if line is to the left, turn left.
    #     left()
    #     break
    #
    # while line_pos > -0.6: # Read as: if line is to the right, turn right.
    #     right()
    #     break


