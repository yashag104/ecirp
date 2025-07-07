print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
c_name=name1+name2
c_name=c_name.lower()
t=c_name.count("t")
r=c_name.count("r")
u=c_name.count("u")
e=c_name.count("e")
l=c_name.count("l")
o=c_name.count("o")
v=c_name.count("v")
e=c_name.count("e")
first_digit=str(t+r+u+e)
second_digit=str(l+o+v+e)
love_score=int(first_digit+second_digit)
if 40<= love_score <=50:
  print(f"Your score is {love_score}, you are alright together.")
elif love_score>=90 or love_score<=10:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
else:
 print(f"Your score is {love_score}.")
  