from plugin import plugin,PYTHON3, require

@require(python=PYTHON3)
@plugin("infob17100")
def infob17100(jarvis, s):
    """Repeats what you type"""
    jarvis.say("Welcome to the info plugin of Rohit Agarwal roll num B17100\n")
    jarvis.say("Please select one of the options below\n")
    jarvis.say("[F]ull Name : print the full name")
    jarvis.say("[H]ometown : print Hometown")
    jarvis.say("Favourite [M]ovie : print favourite movie")
    jarvis.say("Favourite [S]portsperson : print favourite sportsperson")
    jarvis.say("Launch [P]ython program written by me")

    Alpha_command = input("Select your option ")
    if Alpha_command=="F":
        jarvis.say("Rohit Agarwal\n")
    elif Alpha_command=="H":
        jarvis.say("Jaipur\n")
    elif Alpha_command=="M":
        jarvis.say("3 Idiots\n")
    elif Alpha_command=="S":
        jarvis.say("MS Dhoni\n")
    elif Alpha_command == "P":
        jarvis.say("Enter tow numbers. It will return minimum of these two numbers.")
        input1 = input("Enter number 1\n")
        input2 = input("Enter number 2\n")
        ans = min(input1,input2)
        jarvis.say(ans)
    else:
        jarvis.say("Invalid Command\n")
    pass
