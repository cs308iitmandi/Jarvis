from plugin import plugin
import os

@plugin("infob17076")
def infob17076(jarvis, s):
    jarvis.say("Welcome to the info plugin of Aniket roll num B17076. Please select one of the options below:")
    jarvis.say("[F]ull name")
    jarvis.say("[H]ometown")
    jarvis.say("Favourite [M]ovie")
    jarvis.say("Favourite [S]portsperson")
    jarvis.say("Launch [P]ython program written by me")
    s = input();
    if(s == "F"):
        jarvis.say("Aniket Sahu")
    elif(s == "H"):
        jarvis.say("Lucknow")
    elif(s == "M"):
        jarvis.say("Dark Knight")
    elif(s == "S"):
        jarvis.say("Cristiano Ronaldo")
    elif(s == "P"):
        cwd = os.getcwd()
        path = cwd + "/custom/b17076_script.p"
        os.system("python "+path)
    else:
        jarvis.say("Wrong Input");