### Can follow a line:
### Will orient left or right, and drive forward


from motor import Motor
import machine
import sys
from ultrasonic import sonic
from time import sleep
from enum import IntEnum

# --- Configuration --- #
# Digital Sensor Pins
IR_sensors = [21, 20, 19, 18, 17]

# Motor Setup
motor_right = Motor("right", 8, 9, 7)
motor_left = Motor("left", 11,12,13)

# Ultrasonic Sensor Setup
ultrasonic_sensor = sonic(17, 16)

# --- Speed Constants
small = 30
medium = 50
large = 80
delta = 20

# --- State Definition ---
class State(IntEnum):
    straight = 0
    slight_left = 1
    sharp_left = 2
    slight_right = 3
    sharp_right = 4
    search_left = 5
    search_right = 6

# --- Initialization ---
sensors = [machine.Pin(pin, machine.Pin.IN) for pin in IR_sensors]
last_known = State.straight
current = State.straight

# --- Helpers ---
def read_sensors():
    return [s.value() for s in sensors]

def update_state():
    global current, last_known
    bits = read_sensors()
    pattern = (bits[0]<<4 | (bits[1]<<3) | (bits[2]<<2) | (bits[3]<<1) | bits[4])

    if pattern in (0b00100, 0b01110):
        new = State.straight
    elif pattern in (0b01000, 0b11000):
        new = State.slight_left
    elif pattern in (0b10000, 0b11100):
        new = State.sharp_left
    elif pattern in (0b00010, 0b00011):
        new = State.slight_right
    elif pattern in (0b00001, 0b00111):
        new = State.sharp_right
    elif pattern == 0b00000:
        # choose search dir based on last_known
        if last_known in (State.sharp_left, State.slight_left):
            new = State.search_left
        else:
            new = State.search_right
    else:
        # fallback
        new = State.straight

    if new not in (State.search_left, State.search_right):
        last_known = new
    current = new

def apply_state(state):
    """Drive motors according to the chosen state."""
    if state == State.straight:
        motor_left.set_forwards();  motor_left.duty(medium)
        motor_right.set_forwards(); motor_right.duty(medium)

    elif state == State.slight_left:
        motor_left.set_forwards();  motor_left.duty(medium - delta)
        motor_right.set_forwards(); motor_right.duty(medium + delta)

    elif state == State.sharp_left:
        motor_left.set_backwards(); motor_left.duty(small)
        motor_right.set_forwards();  motor_right.duty(large)

    elif state == State.slight_right:
        motor_left.set_forwards();  motor_left.duty(medium + delta)
        motor_right.set_forwards(); motor_right.duty(medium - delta)

    elif state == State.sharp_right:
        motor_left.set_forwards();  motor_left.duty(large)
        motor_right.set_backwards();motor_right.duty(small)

    elif state == State.search_left:
        motor_left.set_backwards(); motor_left.duty(small)
        motor_right.set_forwards();  motor_right.duty(small)

    elif state == State.search_right:
        motor_left.set_forwards();  motor_left.duty(small)
        motor_right.set_backwards();motor_right.duty(small)

# --- Main Loop ---
while True:
    update_state()
    apply_state(current)
    time.sleep(loop_delay)