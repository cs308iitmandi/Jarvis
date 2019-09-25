from plugin import plugin 
import random

def some_prog():
	for i in range(5):
		print("Do nothing random no of times")

@plugin("infob16041")
class infob16041:

	def __call__(self, jarvis, s):
		x = "Welcome to the info plugin of Vishnu Priya Jindal roll num b16041. Please select one of the options below:\n [F]ull name // prints your full name\n [H]ometown // prints your hometownFavourite \n [M]ovie // prints your fav movieFavourite \n [S]portsperson // prints your fav sportspersonLaunch \n [P]ython program written by me // launch a (short)// python program\n"
		u_input = jarvis.input(x)

		if u_input == 'F':
			jarvis.say("Vishnu Priya Jindal")
		elif u_input == 'H':
			jarvis.say("Barnala")
		elif u_input == 'M':
			jarvis.say("ZNMD")
		elif u_input == 'S':
			jarvis.say("Virat Kohli")
		elif u_input == 'P':
			some_prog()
		else:
			jarvis.say("Invalid Input") 
