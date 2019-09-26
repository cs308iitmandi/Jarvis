from plugin import plugin
import os

@plugin("infob17101")
def infoB17101(jarvis, s):
    jarvis.say("Welcome to the info plugin of Sachin roll num B17101. Please select one of the options below:\n[F]ull name // prints your full name\n[H]ometown // prints your hometown\nFavourite [M]ovie // prints your fav movie\nFavourite [S]portsperson // prints your fav sportsperson\nLaunch [P]ython program written by me // launch a (short)// python program")
    inp = input()
    if inp == "F":
        jarvis.say("Sachin S Ranjalkar")
        pass
    if inp == "H":
        jarvis.say("Aurangabad, Maharashtra")
        pass
    if inp == "M":
        jarvis.say("Dazed and Confused")
        pass
    if inp == "S":
        jarvis.say("Cristiano Ronaldo")
        pass
    if inp == "P":
        os.system("python /local/user/my.py")
        pass

