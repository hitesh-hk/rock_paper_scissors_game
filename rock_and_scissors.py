from time import sleep
from os import system
import requests
import random
import sys

'''
rock > scissors
rock < paper

paper > rock
paper < scissors

scissors > paper
scissors <  rock
'''

def bot():
        bruh = ""
        randnum = random.randint(0, 2)
        if randnum == 0:
                bruh = "rock"
        elif randnum == 1:
                bruh = "paper"
        elif randnum == 2:
                bruh = "scissors"
        return bruh



yourscore = 0
botscore = 0
print("welcome to Rock Paper Scissors")
print("its 2 out of 3")
try:

	while True:
		if sys.platform == 'win32':
        		clear = system("cls")
		else:
        		clear = system("clear")
		clear
		if yourscore == 3:
			print("good job, you won want a cookie? Go and buy!!!")
			sleep(2)
			break
		if botscore == 3:
			print("oooof you lost bruhhh :(")
			sleep(2)
			break
		print ("your score: {}".format(yourscore))
		print ("bot score: {}".format(botscore))
		print("Use Ctrl-c to exit from game")
		choice = input("Option: ")
		choice = choice.lower()
		com = bot()
		if choice == com:
			print ("DRAW")
			sleep(2)
			continue
		elif choice == "rock" and com == "scissors":
			print ("you chose rock and bot chose scissors you won")
			sleep(2)
			yourscore += 1
			continue
		elif choice == "rock" and com == "paper":
			print ("you chose rock and bot chose paper, we'll get em next time.")
			sleep(2)
			botscore += 1
			continue
		elif choice == "paper" and com == "rock":
			print ("you chose paper and bot chose rock you won")
			sleep(2)
			yourscore += 1
			continue
		elif choice == "paper" and com == "scissors":
			print ("you chose rock and bot chose paper, we'll get em next time.")
			sleep(2)
			botscore += 1
			continue
		elif choice == "scissors" and com == "paper":
			print ("you chose scissors and bot chose paper you won")
			sleep(2)
			yourscore += 1
			continue
		elif choice == "scissors" and com == "rock":
			print ("you chose rock and bot chose paper, we'll get em next time.")
			sleep(2)
			botscore += 1
			continue

		elif choice != "rock" or choice != "paper" or choice != "scissors" :
			print("Please choose rock, paper, or scissors!")
			sleep(2)
			continue
except KeyboardInterrupt:
	print ("\nCtrl-C Pressed Exiting")
	sleep(1.5)
	exit()
