from plugin import plugin
import os

@plugin('infob17039')
def infob17039(jarvis, s):
	jarvis.say("Welcome to the info plugin of Deepak kumar roll num B17039.")
	jarvis.say("Use letter inside [] to execute: ")
	jarvis.say("[F]ull name") # prints your full name
	jarvis.say("[H]ometown") # prints your hometown
	jarvis.say("Favourite [M]ovie")  # prints your fav movie
	jarvis.say("Favourite [S]portsperson") # prints your fav movie
	jarvis.say("Launch [P]ython program written by me") # prints your fav sportsperson

	option = input("Enter your option: ")
	if option=="F":
		jarvis.say("Deepak kumar\n")
	elif option=="H":
		jarvis.say("India\n")
	elif option=="M":
		jarvis.say("Bahubali\n")
	elif option=="S":
		jarvis.say("Rohit sharma\n")
	elif option=="P":
		os.system("python /local/user/Jarvis/jarviscli/plugins/hello.py")
		print("\n")
	else:
		jarvis.say("Command not found\n")