from plugin import plugin
import os

@plugin("infob17033")
def helloworld(jarvis,s):
    """Repeats what you type"""
    jarvis.say("Welcome to the info plugin of Akhil Rajput roll num b17033.\n\nPlease select one of the options below:\n\n[F]ull name // prints your full name\t\t\t\n[H]ometown // prints your hometown \t\t\t\nFavourite [M]ovie // prints your fav movie  \t\t\t\nFavourite [S]portsperson // prints your fav sportsperson   \t\t\t\nLaunch [P]ython program written by me // launch a (short) // python program\n")
    inf = jarvis.input()
    if(inf=="F"):
    	jarvis.say("Akhil Rajput")
    if(inf=="H"):
    	jarvis.say("Chandigarh")
    if(inf=="S"):
    	jarvis.say("Kento Momota")
    if(inf=="M"):
    	jarvis.say("3 idiots")
    if(inf=="P"):
    	os.system("python /home/akhil/Documents/tech-stack/Jarvis/jarviscli/plugins/akhil.py")