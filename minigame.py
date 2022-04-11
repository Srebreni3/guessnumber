import time
import random

print ("Let's play game. Guess number from 1 to 10")
first_player = int (input("1th player, guess the number: "))
second_player = int (input("2nd player, guess the number: "))
for sec in range (3,0,-1):
    print (sec)
    time.sleep(1)
x = random.randint(1,10)
print ("number is: " + str(x))
if first_player == x:
    print("One point for first player!")
elif second_player  == x:
    print("One point for second player!")
else:
    print("Let's play again!")