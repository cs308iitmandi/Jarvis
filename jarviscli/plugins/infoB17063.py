from plugin import PYTHON3, plugin, require

@require(python=PYTHON3)
@plugin('infob17063')
def infob17063(jarvis, s):
	# """
	# 	Welcome to the info plugin of <your_name> roll num
	# 	<your_roll_num>. Please select one of the options below:
	# 	[F]ull name // prints your full name
	# 	[H]ometown // prints your hometown
	# 	Favourite [M]ovie // prints your fav movie
	# 	Favourite [S]portsperson // prints your fav sportsperson 
	# 	Launch [P]ython program written by me // launch a (short) python program
	# """
	jarvis.say("Welcome to the info plugin of Siddharth Gupta roll num B17063.")
	jarvis.say("Use letter inside [] to execute: ")
	jarvis.say("[F]ull name") # prints your full name
	jarvis.say("[H]ometown") # prints your hometown
	jarvis.say("Favourite [M]ovie")  # prints your fav movie
	jarvis.say("Favourite [S]portsperson") # prints your fav movie
	jarvis.say("Launch [P]ython program written by me") # prints your fav sportsperson

	option = input("Select your option: ")
	if option=="F":
		jarvis.say("Siddharth Gupta\n")
	elif option=="H":
		jarvis.say("Alwar\n")
	elif option=="M":
		jarvis.say("Avengers:Endgame\n")
	elif option=="S":
		jarvis.say("Virat Kohli\n")
	elif option=="P":
		jarvis.say("Enter two numbers. It will print max of the two.\n")
		input1 = input("Enter 1st Number: ")
		input2 = input("Enter 2nd Number: ")
		ans = max(float(input1), float(input2))
		print("Max of the two is: ", ans)
		print("\n")
	else:
		jarvis.say("Invalid Command.\n")



