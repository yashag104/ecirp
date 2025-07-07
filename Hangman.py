import random
import Hangman_art
import Hangman_words
import Hangman_stages
print(Hangman_art.logo)
word=random.choice(Hangman_words.word_list)
#print(word)
blank_list=[]
for num in range(len(word)):
    blank_list.append("_")
print(blank_list)
lives=6
while "_" in blank_list and lives > 0:
    guess_letter=input("Guess a Letter: ").lower()
    num=0    
    for letter in word:
        if letter==guess_letter:
            blank_list[num]=letter
        num+=1
    print(blank_list) 
    if guess_letter not in word:
        lives -=1
    elif guess_letter in blank_list:
        print("You have already entered a letter")
    print(Hangman_stages.stages[lives])    
if lives==0:
    print(f"You lose!, word was {word}")
else:        
    print("You won!")   