from plugin import plugin
import os

@plugin("infob17120")
def helloworld(jarvis, s):
	print("Welcome to the info plugin of Deepshikha Rana roll num B17120. Please select one of the options below:\n[F]ull name // prints your full name\n[H]ometown // prints your hometownFavourite \n[M]ovie // prints your fav movieFavourite \n[S]portsperson // prints your fav sportspersonLaunch \n[P]ython program written by me // launch a (short)// python program")
	val = input()
	if(val=='F'):
		jarvis.say("Deepshikha Rana\n")
	elif(val=='H'):
		jarvis.say("Haryana\n")
	elif(val=='M'):
		jarvis.say("Super 30\n")
	elif(val=='S'):
		jarvis.say("MS DHONi\n")
	elif(val=='P'):
		os.system("python ~/Jarvis/custom/a.py")
		# jarvis.say("Python\n")
	else:
		jarvis.say("Invalid Input")	
	"""Repeats what you type"""
	# jarvis.say(s)