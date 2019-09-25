from plugin import plugin
import os

@plugin("b17068")
def b17068(jarvis, s):
    jarvis.say("f - full name\nh - Home Town\nm - favourite movie\ns - sports person\np - launch python program\n")
    in = jarvis.input()
    if(in==f):
        jarvis.say("Vinay Kumar")
    if(in=='h'):
        jarvis.say("Gorakhpur")
    if(in=='m'):
        jarvis.say("Star Wars")
    if(in=='s'):
        jarvis.say("MS Dhoni")
    if(in=='p'):
        os.system("python /home/vinay/Documents/Jarvis/jarviscli/plugins/pro.py")




