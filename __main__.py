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

# Put your code to execute in this function here
def main():
    # To print text to the terminal window, use the print() function like this:
    print("Starting program...")
    # Printing to the terminal window is a good way to debug your code

    # First, we create an object of the controller. We will use this to access functions within the Controller class
    print("Creating a new controller object")
    controller = idl_controller.Controller()
    print("Controller object successfully created")

    # print("Driving straight for 4 seconds...")
    controller.driveStraight(4)
    # print("Stopping for 3 seconds...")
    # controller.stop(3)
    # print("Turning for 5 seconds...")
    # controller.turn(5)
    print(controller.getDistance())

# When we execute the program, the main function is called
if __name__=="__main__":
    main()