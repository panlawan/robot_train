from gpiozero import Motor
from time import sleep

left_motor = Motor(forward=5, backward=6)
right_motor = Motor(forward=21, backward=26)

left_motor.forward()
right_motor.forward()
print("Forward")
sleep(2)

left_motor.backward()
right_motor.backward()
print("Backward")
sleep(2)

left_motor.stop()
right_motor.stop()
print("Stop")
