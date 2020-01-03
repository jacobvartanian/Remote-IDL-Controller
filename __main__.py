"""
This is the main python file that will run when you execute the program.

Here, you will add your code to control your device. Follow the instructions
beginning with a '#' symbol. Any line with this symbol at the start of it
indicates it is an internal comment and will not interfere with the program.

Look for the TODO flag (to-do) indicating that you will need to add/modify some
code here.

Make sure you SAVE regularly and backup your code online before you log out.

WARNING: FILES SAVED LOCALLY MAY BE DELETED AUTOMATICALLY WHEN YOU LOG OUT
"""

# We need to import the code from the idl_controller package so we can access its functions
import idl_controller

def mainTutorial():
    # To print text to the terminal window, use the print() function like this:
    print("Starting program...")
    # Printing to the terminal window is a good way to debug your code

    # First, we create an object of the controller. We will use this to access functions within the Controller class
    print("Creating a new controller object")
    controller = idl_controller.Controller()
    print("Controller object successfully created")

    # To drive the device forward for a number of seconds, we use the function, driveStraight() like this:
    print("Driving straight for 4 seconds...")
    controller.driveStraight(control_time = 4, direction = controller.FORWARD)

    # To drive the device in reverse for a number of seconds, we use the function, driveStraight() like this:
    print("Driving in reverse for 3 seconds...")
    controller.driveStraight(control_time = 3, direction = controller.REVERSE)

    # To stop the device, we use the function, stop() like this:
    print("Stopping for 3 seconds...")
    controller.stop(stop_time = 3)

    # To turn the device, we use the function, turn() like this:
    print("Turning for 5 seconds...")
    controller.turn(control_time = 5, direction = controller.CLOCKWISE)

    # TODO Activity 1:
    # Modify the above code so your device performs the following tasks:
    # 1. Move forward for 5 seconds
    # 2. Stop for 2 seconds
    # 3. Turn counter-clockwise for 3 seconds
    # 4. Move in reverse for 1 second

    # We are now able to control the robot for a number of seconds, but let's make use of the onboard sensors to control it

    # To get the distance from the time of flight sensor, we use the function, getDistance() like this:
    distance = controller.getDistance()
    print("Distance:\t{0}".format(distance))

    # To get the heading from the magnetometer, we use the function, getHeading() like this:
    heading = controller.getHeading()
    print("Heading:\t{0}".format(heading))

    # To drive and turn the device without stopping, simply call the driveStraight() and turn() functions
    # but leave out the control_time parameter like this:
    print("Driving straight...")
    controller.driveStraight(direction = controller.FORWARD)

    # The motors have turned on and will continue to move until you tell it to stop
    # We can use the delayMilliseconds function to wait a number of milliseconds
    print("Waiting 2000 milliseconds (2 seconds)...")
    controller.delayMilliseconds(2000)

    # Now let's stop the motors for 3 seconds
    controller.stop(stop_time = 3)

    # Let's say we want to drive until the distance is less than 30cm. In code, we can read this as:
    # 1. Turn the motors on to dirve forward
    controller.driveStraight(direction = controller.FORWARD)

    # 2. While the distance is greater than 30, wait
    distance = controller.getDistance()
    while distance > 30:
        distance = controller.getDistance()
        controller.delayMilliseconds(10)

    # 3. Stop the motors
    controller.stop()

    # TODO Activity 2:
    # Repeat the above steps for the turning function. We want the robot to point between 200 and 220 degrees
    # 1. Turn the motors on to turn clockwise
    # 2. While the heading is greater than 220 degrees or less than 200 degrees, wait
    # HINT: Use the 'or' keyword
    # 3. Stop the motors

# TODO Activty 3:
# Put your code to execute in this function here. 
def main():
    # To print text to the terminal window, use the print() function like this:
    print("Starting program...")
    # Printing to the terminal window is a good way to debug your code

    # First, we create an object of the controller. We will use this to access functions within the Controller class
    print("Creating a new controller object")
    controller = idl_controller.Controller()
    print("Controller object successfully created")

# When we execute the program, the mainTutorial function is called
if __name__=="__main__":
    mainTutorial()
    # When you are ready to test your main method, replace mainTutorial() with main()