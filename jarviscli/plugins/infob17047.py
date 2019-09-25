from plugin import plugin
import os

@plugin("infob17047")
def infob17047(jarvis, s):
    """Repeats what you type"""
    jarvis.say("Welcome to the info plugin of <your_name> roll num <your_roll_num>. Please select one of the options below:\n[F]ull name // prints your full name\n[H]ometown // prints your hometown\nFavourite [M]ovie // prints your fav movie\nFavourite [S]portsperson // prints your fav sportsperson\nLaunch [P]ython program written by me")
    g = input("Enter your command : ")
    s=str("F")
    if(g==s):
    	jarvis.say("Kanika Gupta")

    s=str("H")
    if(g==s):
    	jarvis.say("Karnal")

    s=str("M")
    if(g==s):
    	jarvis.say("Shawshank")
    s=str("S")
    if(g==s):
    	jarvis.say("blabla")
    s=str("P")
    if(g==s):
    	os.system("python /local/user/Jarvis/jarviscli/plugins/hello.py")
