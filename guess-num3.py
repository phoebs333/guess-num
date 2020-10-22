# Produce a random number 1~100 (Don't print)
# Repeat the guessing
# If the answer is correct, print ('Bingo!')
# If the answer is wrong, tell the user if the guess is larger or smaller than the answer.

import random
start = input ('Please define a start number:')
end = input ('Please define an end number:')
start = int (start)
end = int (end)

r = random.randint(start, end)
count = 0
while True:
    count += 1 # count = count + 1
    num = input ('Please guess a number:')
    num = int (num)
    if num == r:
        print ('Bingo!')
        print ('No. of guess:', count)
        break
    elif num > r:
    	print ('Your guess is larger than the answer.')
    elif num < r:
    	print ('Your guess is smaller than the answer.')
    print ('No. of guess:', count)