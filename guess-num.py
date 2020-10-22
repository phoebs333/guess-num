# Produce a random number 1~100 (Don't print)
# Repeat the guessing
# If the answer is correct, print ('Bingo!')
# If the answer is wrong, tell the user if the guess is larger or smaller than the answer.

import random

r = random.randint(1,100)
while True:
    num = input('Please guess a number:')
    num = int (num)
    if num == r:
    	print ('Bingo!')
    	break
    elif num > r:
    	print ('Your guess is larger than the answer.')
    elif num < r:
    	print ('Your guess is smaller than the answer.')
