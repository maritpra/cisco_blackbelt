#!/usr/bin/env python3

from random import randint

number = randint(1,10)
guess = 0
while True:
	guess = input("Guess the number:")
	print("Wrong, try again!\n")
	if int(guess) == number:
		break
	
print("Correct!")

	
	




