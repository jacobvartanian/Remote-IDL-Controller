from idl_controller.controller import Controller

TOKEN = "SAMPLE_TOKEN"

def main():
    controller = Controller(TOKEN)
    print("Driving straight for 4 seconds...")
    controller.driveStraight(4)
    print("Stopping for 3 seconds...")
    controller.stop(3)
    print("Turning for 5 seconds...")
    controller.turn(5)

if __name__=="__main__":
    main()