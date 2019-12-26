from idl_controller.controller import Controller

TOKEN = "xfT1Wz7ju6nZAfGhFxyGktFFLVCpGtxO"

def main():
    controller = Controller(TOKEN)
    # print("Driving straight for 4 seconds...")
    # controller.driveStraight(4)
    # print("Stopping for 3 seconds...")
    # controller.stop(3)
    # print("Turning for 5 seconds...")
    # controller.turn(5)
    print(controller.getDistance())

if __name__=="__main__":
    main()