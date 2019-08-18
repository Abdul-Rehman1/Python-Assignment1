# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 12:30:33 2019

@author: Abdul Rehman
"""

import random
lst=("first","second","third","fourth","fifth")
print("Guess Number from [1 to 10]\n You have to guess the number with in 5 trials")
numToGuess = random.randint(1,  10)
count=0
guessedNum = int(input("Enter a number to guess "+lst[count]+" trail:"))
while(numToGuess!=guessedNum and count<4):  
    count+=1
    print("Inputed number was not matched with the number to be guessed")
    guessedNum = int(input("Enter a different number to guess "+lst[count]+" trail:"))
    
if count<4:    
    if numToGuess==guessedNum: 
        print(f"You win, you guessed the number in your {lst[count]} trial");
else:
    print("Sorry You have completed you 5 tries and can not guess the number");         