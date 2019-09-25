from plugin import plugin
import os

@plugin("infob17028")
def info_b17009(jarvis, s):
    jarvis.say("Welcome to the info plugin of Tanmay roll num B17028. Please select one of the options below:")
    jarvis.say("[F]ull name")
    jarvis.say("[H]ometown")
    jarvis.say("Favourite [M]ovie")
    jarvis.say("Favourite [S]portsperson")
    jarvis.say("Launch [P]ython program written by me")
    s = input();
    if(s == "F"):
        jarvis.say("Tanmay Rustagi")
    elif(s == "H"):
        jarvis.say("Delhi")
    elif(s == "M"):
        jarvis.say("Kimi No Nawa")
    elif(s == "S"):
        jarvis.say("Ma Long")
    elif(s == "P"):
        jarvis.say("Running")
        cwd = os.getcwd()
        path = cwd + "/custom/script.p"
        os.system("python "+path)
    else:
        jarvis.say("Unrecognised option - " + s);