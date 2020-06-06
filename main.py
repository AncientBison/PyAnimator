from UsefulCommands import *
import time
import os
import shutil
import requests

def rules():
	sprint(Cyan + "RULES\nTo end the scene click enter and type, \"#EndScene\".\nTo end the animation click enter and type, \"#EndAnimation\".\nIf you make a mess up go to the file editor and change the frame in witch you messed up.")

solditems = requests.get('https://raw.githubusercontent.com/AncientBison/Animation/master/README.md')
data = solditems.content
with open('data.json', 'wb') as f:
  f.write(data)

def getScene(n,DIR):
	global name
	with open("{}/{}.txt".format(DIR,n)) as f:
		s = f.read()
		return s

def example():
	play("example", 1)
	sprint(Cyan + "Now you try!")
	rules()


def play(directory,second):
	fileList = next(os.walk(directory))
	count = len(fileList[2])
	print("\x1b[3J\x1b[H\x1b[2J")
	for n in range(1, count + 1):
		print(getScene(n,directory))
		time.sleep(second)
		print("\x1b[3J\x1b[H\x1b[2J")


def editor():
	name = ask("What would you like you animation to be called?\n>> ")
	os.makedirs(name, exist_ok=True)
	n = 0
	string = ""
	while True:
		newString = input()
		if newString in ["#EndScene", "#EndAnimation"]:
			n += 1
			with open(os.path.join(
					name, "{}.txt".format(str(n))), "w") as f:
				f.write(string)
			string = ""
			print("\x1b[3J\x1b[H\x1b[2J")
			if newString == "#EndAnimation":
				play(name,1)
				break
		else:
			string += "\n" + newString

def start():
	sprint(Cyan + "Welcome to PyAnimator!")
	answer = ask(Cyan + "Would you like to see an example? [y/n]" + Reset + "\n>> ")
	if answer == "y":
		example()
	elif answer == "n":
		rules()
		editor()
start()
