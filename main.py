import os
import sys
import ctypes
import time
def main():
	global text
	text = ""
	error_log = open("errors.log", "a")
	sys.stderr = error_log
	ctypes.windll.kernel32.SetConsoleTitleW("Letter creator.")
	print("Letter creator 1.0.")
	print("Written by Ty Gillespie.")
	print("Press enter to begin.")
	input()
	print("Type the greeting of your letter, for example, dear.")
	greeting = input()
	if greeting == "":
		print("A greeting wasn't entered.")
		print("Press enter to exit.")
		input()
		sys.exit()
	else:
		text += greeting + " "
	print("Type the name of the person that will be receving this letter, and press enter.")
	name = input()
	if name == "":
		print("A name wasn't entered.")
		print("Press enter to exit.")
		input()
		sys.exit()
	else:
		text += name + ",\n"
	print("Type the text of your letter.")
	print("When you're done, type the word \"done\" on a new line.")
	while True:
		time.sleep(0.005)
		next_line = input()
		if next_line.replace(" ", "").lower() == "done":
			break
		else:
			text += next_line + "\n"
			continue
	print("Now type the closing of your letter, without your name and without the comma.")
	closing = input()
	if closing == "":
		print("A closing wasn't entered.")
		print("Press enter to exit.")
		input()
		sys.exit()
	else:
		text += closing + ",\n"
	print("And finally, type your name.")
	your_name = input()
	if your_name == "":
		print("A name wasn't entered.")
		print("Press enter to exit.")
		input()
		sys.exit()
	else:
		text += your_name
	if os.path.isfile("Letter to " + name + ".txt"):
		print("Error: file already exists!")
		print("Press enter to exit.")
		input()
		sys.exit()
	else:
		f = open("Letter to " + name + ".txt", "a")
		f.write(text)
		f.close()
		print("The letter was created.")
		print("It is in the same directory as this program, in a file called ")
		print("Letter to " + name + ".txt.")
		print("Press enter to exit.")
		input()
		sys.exit()
if __name__ == "__main__":
	main()