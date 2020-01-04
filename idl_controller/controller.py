import time
from .virtual_pins import *
from .remote import Remote

MAX_SPEED = 57
MAX_STEER = 10

DEFAULT_CONTROL_TIME_SECONDS = 0.1

class Controller():
    def __init__(self):
        self._remote = Remote()

    FORWARD = 1
    REVERSE = -1
    def driveStraight(self, control_time = None, direction = FORWARD, speed = MAX_SPEED):
        """Moves the device in a straight line for a given time before stopping

        Note: This function is BLOCKING

        Keyword arguments:
        control_time -- How long to move the device for before stopping. If None (default),
        this function will be non-blocking and the device will not stop
        direction -- FORWARD or REVERSE (note: you may need to type "Controller." before the keyword)
        speed -- How fast to move the device (maximum = 57)
        """
        if direction in [self.FORWARD, self.REVERSE]:
            drive_success = self.setDrive(direction * speed, 0)
            stop_success = True
            if control_time:
                time.sleep(control_time)
                stop_success = self.stop()
            return drive_success and stop_success
        return False

    # TODO Verify this with hardware
    CLOCKWISE = 1
    COUNTER_CLOCKWISE = -1
    def turn(self, control_time = None, direction = CLOCKWISE, speed = MAX_SPEED):
        """Turns the device on the spot for a given time before stopping

        Note: This function is BLOCKING

        Keyword arguments:
        control_time -- How long to move the device for before stopping. If None (default),
        this function will be non-blocking and the device will not stop
        direction -- CLOCKWISE or COUNTER_CLOCKWISE (note: you may need to type "Controller." before the keyword)
        speed -- How fast to move the device (maximum = 57)
        """
        if direction in [self.CLOCKWISE, self.COUNTER_CLOCKWISE]:
            drive_success = self.setDrive(direction * speed, MAX_STEER)
            stop_success = True
            if control_time:
                time.sleep(control_time)
                stop_success = self.stop()
            return drive_success and stop_success
        return False
    
    def stop(self, stop_time = 0):
        """Stops the device

        Note: This function is BLOCKING

        Keyword arguments:
        stop_time -- How long to stop the device for.
        """
        success = self.setDrive(0, 0)
        time.sleep(stop_time)
        return success
    
    def setDrive(self, speed, steer):
        """Sets the speed and steer parameters of the device. Note: this will NOT stop the device when completed

        Note: This function is NOT BLOCKING

        Keyword arguments:
        speed -- The value to set the speed parameter to
        speed -- The value to set the steer parameter to
        """
        if speed > MAX_SPEED:
            speed = MAX_SPEED
        if speed < -MAX_SPEED:
            speed = -MAX_SPEED
        if steer > MAX_STEER:
            steer = MAX_STEER
        if steer < -MAX_STEER:
            steer = -MAX_STEER
        return self._remote.publish(MobilitySpeed_Vpin, speed) and self._remote.publish(MobilitySteer_Vpin, steer)

    def getDistance(self):
        """Gets the distance reported by the time of flight sensor

        Returns:
        The distance reported by the time of flight sensor as a float
        """
        json_data = self._remote.subscribe(Distance_Vpin)
        if json_data:
            return float(json_data[0])
        return False

    def getHeading(self):
        """Gets the heading reported by the magnetometer

        Returns:
        The heading reported by the magnetometer as a float
        """
        json_data = self._remote.subscribe(Heading_Vpin)
        if json_data:
            return float(json_data[0])
        return False
    
    # TODO Extension Activity
    # Implement your own methods to get and set other values on the IDL
    # Refer to http://iot.nortcele.win/doc/reference/virtual-pins.html
    # for further information on what functionality the IDL has

    def delaySeconds(self, delay):
        """Pause the program for a number of seconds
        """
        time.sleep(delay)
        return True
    
    def delayMilliseconds(self, delay):
        """Pause the program for a number of milliseconds
        """
        time.sleep(delay / 1000)
        return True