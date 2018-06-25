#!/usr/bin/env python3

from random import randint

number = randint(1,10)
#print(number)
guess = 0
while guess != number:
	guess = int(input("Guess the number:"))
	if guess != number:
		print("Wrong, try again!\n")
	else:
		print("Correct!")


	
	




