# Car game, prompt commands

command = ""
AlreadyStarted = False
AlreadyStopped = False

while True:
    command = input('> ').lower()

    if command == "start":
        if AlreadyStarted:
            print("Car has already started.. ")
        else:
            print("Car started.. Ready to GO!!")
            AlreadyStarted = True

    elif command == "stop":
        if not AlreadyStarted:
            print("Car is already stopped")
        else:
            print("Car Stopped..")
            AlreadyStarted = False

    elif command == "quit":
        break

    elif command == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print('quit - to exit')

    else:
        print("I don't understand you..")
