import os
import secret_auction_art
print(f"{secret_auction_art.logo}\n Welcome to secret auction.")
to_countinue=True
bidders={}
bidder=[]
num=0
while to_countinue:
    name=input("What is your name?: ")
    bid=float(input("What is you bid?: $"))
    bidders[name]=bid
    bidder.append([name,bid])
    num +=1
    check=input("Are there any other bidders? Type 'yes' or 'no'." )
    if check=="no":
        to_countinue=False
    os.system('cls')
max_name=bidder[0][0]
max=bidder[0][1]
i=0
for i in range(1,num):
    if max < bidder[i][1]:
        max_name=bidder[i][0]
        max=bidder[i][1]
print(f"The winner is {max_name} with a bid of ${max}.")        