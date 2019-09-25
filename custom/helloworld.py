from plugin import plugin
import os

@plugin("infob17060")
def helloworld(jarvis,s):
    """Repeats what you type"""
    jarvis.say("Welcome to the info plugin of <your_name> roll num <your_roll_num>.\n\nPlease select one of the options below:\n\n[F]ull name // prints your full name\t\t\t\n[H]ometown // prints your hometown \t\t\t\nFavourite [M]ovie // prints your fav movie  \t\t\t\nFavourite [S]portsperson // prints your fav sportsperson   \t\t\t\nLaunch [P]ython program written by me // launch a (short) // python program\n")
    inf = jarvis.input()
    if(inf=="F"):
    	jarvis.say("Saurbh")
    if(inf=="H"):
    	jarvis.say("New Delhi")
    if(inf=="S"):
    	jarvis.say("Dhoni")
    if(inf=="M"):
    	jarvis.say("Bhool Bhulaiya")
    if(inf=="P"):
    	os.system("python /local/user/Desktop/lab7/Jarvis/saurbh.py")


