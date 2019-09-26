from plugin import plugin
import os

@plugin('infob17065')

def info(jarvis, s):

	def help():

		jarvis.say('Welcome to the info plugin of Vaibhav Saharan Roll num B17067. Please select one of the options below:')
		jarvis.say('[F]ull name')
		jarvis.say('[H]ometown')
		jarvis.say('Favourite [M]ovie')
		jarvis.say('Favourite [S]portsperson')
		jarvis.say('Launch [P]ython program written by me')
		jarvis.say('[Q]uit')
		jarvis.say('[h]elp')

	help()
	while 1:
		ch=input()
		if ch=='F':
			jarvis.say('Vaibhav Saharan')
		elif ch=='H':
			jarvis.say('Ajmer')
		elif ch=='M':
			jarvis.say('Forrest gump')
		elif ch=='S':
			jarvis.say('Halie Gebrselassie')
		elif ch=='P':
			os.system("python ~/python/addnum.py")
		elif ch=='Q':
			break
		elif ch=='h':
			help()
		else:
			jarvis.say('Invalid option Please type F or H or M or S or P')