command = ""
started = True
stopped = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            print("Car started")
    elif command == "stop":
        if stopped:
            print("Car is already stopped")
        else:
            print("Car stopped")
    elif command == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to exit
        ''')
    elif command == "quit":
        break
    else:
        print("I do not understand")