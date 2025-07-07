rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
game=[rock, paper, scissors]
user=int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors. "))
if user>=3 and user<0:
 print("You choose an invalid number")
else: 
 print(game[user])
 print("computer choose:")
 computer=random.randint(0,2)
 print(game[computer])
 if computer==user:
  print("Drawn")
 if computer==0:
  if user==1:
   print("You Won!")
  else:
   print("You lose!")
 elif computer==1:
  if user==0:
    print("You lose!")  
  else:
    print("You Won!") 
 else:
  if user==0:
   print("You Won!")
  else:
   print("You lose!")     



