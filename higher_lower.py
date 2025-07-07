import hl_art
from hl_data import data
import random
from os import system
system('cls')
print(hl_art.logo)
key=True
score=0
wrong=0
while key:
    n1=random.choice(data)
    n2=random.choice(data)
    while n1==n2:
        n2=random.choice(data)
    print(f"Comapre A: {n1['name']}, {n1['description']}, from {n1['country']}")
    print(hl_art.vs)
    print(f"Against B: {n2['name']}, {n2['description']}, from {n2['country']}") 
    choice=input("Who has the more followers? Type 'A' or 'B': ")
    if choice.lower()=="a" and int(n1['follower_count'])>int(n2['follower_count']):
        score +=1
        system('cls')
        print(f"You were right! Current Score: {score}")
    elif choice.lower()=="b" and int(n1['follower_count'])<int(n2['follower_count']):
        score +=1
        system('cls')
        print(f"You were right! Current Score: {score}") 
    else:
        wrong +=1
        system('cls')
        print(f"Sorry, that's wrong. Current score: {score}") 
    if wrong==2:
        if choice.lower()=="a" and int(n1['follower_count'])>int(n2['follower_count']):
            system('cls')
            print(f"You were right! Final Score: {score}")
        elif choice.lower()=="b" and int(n1['follower_count'])<int(n2['follower_count']):
            system('cls')
            print(f"You were right! Final Score: {score}")          
        key=False