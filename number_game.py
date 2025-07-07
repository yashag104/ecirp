import os
import random
import number_game_art
key= True

while key:
    print(number_game_art.logo)
    print("Welcome to the Number Guessing Game!")
    number=random.randint(1,100)
    guess=0
    level=input("Choose a difficulty level. 'Easy' or 'Hard': ").lower()
    if level=="easy":
        guess=10
    else:
        guess=5
    print(f"You have {guess} attempts remaining to guess the number.")    
    result=False
    while guess!=0 and not result:
        no=int(input("Make a guess: "))
        if no==number:
            print(f"You got it! The answer was {number}.")  
            result=True
        elif no>(number):
            print(f"Too high")
            guess -=1 
            print(f"You have {guess} attempts remaining to guess the number.")    
        elif no<(number):
            print(f"Too low")
            guess -=1 
            print(f"You have {guess} attempts remaining to guess the number.")    
        elif no<(number) and no>number-5:
            print(f"Low but close.")
            guess -=1 
        elif no>(number) and no<number+5:
            print(f"High but close.")
            guess -=1
        else:
            print(f"Guess Again!") 
            guess -=1 
    if guess==0:
        print(f"You Lose. The answer was {number}")
    choice=input("Do you want to play again? type 'y' or 'n': ")
    if choice=="n":
        key=False
    os.system('cls')                              