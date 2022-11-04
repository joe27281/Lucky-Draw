import random
import ctypes
import time

ctypes.windll.kernel32.SetConsoleTitleA("Lucky Draw")

rounds = 1

def line(size):
	if size == "big":
		print("-------------------------")
		if rounds == 1:
			print("First Round Starting!")
			time.sleep(1)
			print("")
		else:
			print("New Round Starting!")
			print("")
	elif size == "small":
		print("-------------")
		if rounds == 1:
			print("First Round Starting!")
			time.sleep(1)
			print("")
		else:
			print("New Round Starting!")
			print("")

#debug = str(input("Would you like to put DEBUG mode on? [yes/no]: ")).upper()
#if debug == "YES":
#	debug = 1
#	print("yes")
#else:
#	debug = 0

def space():
	print("")

print("The goal of the game is to guess the correct number 7 times consecutively.")
print("Every round you get wrong sets you back to round 1.")

while True:
	ready = str(input("Are you ready? [y/n] ")).upper()
	if ready == "Y":
		line("big")
		break
	else:
		continue


while True:
	c1 = (random.randint(1, 10000))
	c2 = (random.randint(1, 10000))
	c3 = (random.randint(1, 10000))
	c4 = (random.randint(1, 10000))
	number = [c1, c2, c3, c4]
	ans = random.choice(number)
	print("A number has been selected.")
	space()
	print("Round",rounds,"of 7")
	print("Which of these is the number?")
	space()
	c1 = str(c1)
	c2 = str(c2)
	c3 = str(c3)
	c4 = str(c4)
	print(c1, "|", c2, "|", c3, "|", c4)
	space()
	guess = int(input("What is your guess of number? "))
	if guess != ans:
		print("")
		print("Incorrect. The correct answer was", ans)
		time.sleep(1)
		line("big")
		rounds = 1
		continue
	else:
		print("Correct!")
		time.sleep(1)
		line("big")
		rounds += 1
		if rounds == 8:
			break
		else:
			continue
#	else:
#		print(ans, "ANSWER (DEBUG)")
#		guess = int(input("What is your guess of number? "))
#		if guess != ans:
#			print("")
#			print("Incorrect. Answer was", ans)
#			time.sleep(1)
#			line("big")
#			rounds = 1
#			continue
#		else:
#			print("Correct!")
#			time.sleep(1)
#			line("big")
#			rounds += 1
#			if rounds == 8:
#				break
#			else:
#				continue

print("You have beaten the lucky draw!")
close = input("Press 'Enter' to close the game.")