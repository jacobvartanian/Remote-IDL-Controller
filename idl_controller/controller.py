import time
from .virtual_pins import *
from .remote import Remote

MAX_SPEED = 57
MAX_STEER = 10

DEFAULT_CONTROL_TIME_SECONDS = 0.1

class Controller():
    def __init__(self, token):
        self._remote = Remote(token)

    FORWARD = 1
    REVERSE = -1
    def driveStraight(self, control_time = DEFAULT_CONTROL_TIME_SECONDS, direction = FORWARD, speed = MAX_SPEED):
        if direction in [self.FORWARD, self.REVERSE]:
            drive_success = self.setDrive(direction * speed, 0)
            time.sleep(control_time)
            stop_success = self.stop()
            return drive_success and stop_success
        return False

    # TODO Verify this with hardware
    CLOCKWISE = 1
    COUNTER_CLOCKWISE = -1
    def turn(self, control_time = DEFAULT_CONTROL_TIME_SECONDS, direction = CLOCKWISE, speed = MAX_SPEED):
        if direction in [self.CLOCKWISE, self.COUNTER_CLOCKWISE]:
            drive_success = self.setDrive(direction * speed, MAX_STEER)
            time.sleep(control_time)
            stop_success = self.stop()
            return drive_success and stop_success
        return False
    
    def stop(self, stop_time = 0):
        success = self.setDrive(0, 0)
        time.sleep(stop_time)
        return success
    
    def setDrive(self, speed, steer):
        return self._remote.publish(MobilitySpeed_Vpin, speed) and self._remote.publish(MobilitySteer_Vpin, steer)

    def getDistance(self):
        # TODO implement this
        return False

    def getHeading(self):
        # TODO implement this
        return False