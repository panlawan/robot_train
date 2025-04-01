from gpiozero import Motor, PWMOutputDevice
from time import sleep

left_motor = Motor(forward=5, backward=6)
right_motor = Motor(forward=21, backward=26)

# PWM for Speed Control
left_speed = PWMOutputDevice(13)
right_speed = PWMOutputDevice(19)

# setup speed  (from 0.0 to 1.0)
def set_speed(speed=0.5):
    left_speed.value = speed
    right_speed.value = speed

# test movement function
def test_movement():
    set_speed(0.6)

    print("Forward")
    left_motor.forward()
    right_motor.forward()
    sleep(2)

    print("Turn Left")
    left_motor.backward()
    right_motor.forward()
    sleep(2)

    print("Turn Right")
    left_motor.forward()
    right_motor.backward()
    sleep(2)

    print("Backward")
    left_motor.backward()
    right_motor.backward()
    sleep(2)

    print("Stop");
    left_motor.stop()
    right_motor.stop()

test_movement()
