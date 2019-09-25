from plugin import plugin
from colorama import Fore, Style


@plugin("infob17058")
def helloworld(jarvis, s):
	""" A plugin by Satyam, student of 3rd year Btech.
		Use this plugin to learn more about me"""

	jarvis.say(Fore.GREEN + "Welcome to the info plugin of Satyam roll num B17058.") 
	jarvis.say(Fore.CYAN + "Please select one of the options below:")
	jarvis.say("\t[F]ull name")
	jarvis.say("\t[H]ometown") 
	jarvis.say("\t[M]ovie") 
	jarvis.say("\t[S]portsperson") 
	jarvis.say("\t[P]ython program written by me")
	jarvis.say(Fore.CYAN + '\t Press "q" to quit')
    # Implementation of above operations
	while(True):
		# take input
		t = jarvis.input()
		# if user wants to quit
		if t == 'q' or t == 'Q':
			jarvis.say("GoodBye ;) ")
			break
		# to print the required detail	
		if t == 'F':
			jarvis.say("My full name is Satyam Shukla")
		elif t == 'H':
			jarvis.say("My hometown is Osaka Japan")
		elif t == 'M':
			jarvis.say('My favourite movie is "Usual Suspects" ')
		elif t == 'S':
			jarvis.say('My favourite sportsperson is "Lionel Messi" ')
		elif t == 'P':
			jarvis.say('Welcome to my python program. This program concatenates two strings puts a space between them')
			jarvis.say('Enter string 1 :')
			a = jarvis.input()
			jarvis.say('Enter string 2 :')
			b = jarvis.input()
			jarvis.say('\tResultant string is : '+a+ ' '+b)					

