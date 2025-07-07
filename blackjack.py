import random
import os
import blackjack_art

def calculate_score(l_cards):
    if sum(l_cards) == 21 and len(l_cards) == 2:
        return 0
    elif 11 in l_cards and sum(l_cards) > 21:
        l_cards.remove(11)
        l_cards.append(1)
        return sum(l_cards)
    else:    
        return sum(l_cards)

def result(user_cards,computer_cards):
    if calculate_score(user_cards)>21:
        print("You went over.You lose")
    elif calculate_score(user_cards)==0:
        print("You WIN with a BLACKJACK!")
    elif calculate_score(computer_cards)==0:
        print("Opponent WIN with a BLACKJACK!")
    elif calculate_score(user_cards)>calculate_score(computer_cards) and calculate_score(user_cards)<22:
        print("You won!")
    elif calculate_score(user_cards)==calculate_score(computer_cards):
        print("Game Drawn!")  
    elif calculate_score(computer_cards) > 21:
        print("Opponent went over. You win")
    else:
        print("You lose.")    

def play_game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    key=True
    while key:
        print(blackjack_art.logo)
        user_cards=[]
        computer_cards=[]
        for card in range(2):
            computer_cards.append(random.choice(cards))
            user_cards.append(random.choice(cards))
        print(f"    Your cards: {user_cards}, current score:{calculate_score(user_cards)}")
        print(f"    Computer's first card: {computer_cards[0]}")
        ch=input("Type 'y' to get another card, type 'n' to pass: ").lower()
        k1=False
        if ch=="y":
            k1=True
        while k1:
            user_cards.append(random.choice(cards))
            print(f"    Your cards: {user_cards}, current score:{calculate_score(user_cards)}")
            if calculate_score(user_cards)>21:
                ch="n"
            else: 
                ch=input("Type 'y' to get another card, type 'n' to pass: ")
            print(f"    Computer's first card: {computer_cards[0]}")
            if ch=="n":
                k1=False
        while calculate_score(computer_cards)<17 and calculate_score(computer_cards)!=0:
            computer_cards.append(random.choice(cards))
        print(f"Your final hand: {user_cards}, final score:{calculate_score(user_cards)}")
        print(f"Computer final hand: {computer_cards}, final score:{calculate_score(computer_cards)}")             
        result(user_cards,computer_cards)
        uch=input("Do you want to play another game of BlackJack? Type 'y' or 'n': ").lower()
        if uch=="n":
            key=False
            os.system('cls')  
        elif uch=="y":
            os.system('cls')
play_game()                