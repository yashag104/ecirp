# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
w = int(nr_letters-nr_numbers-nr_symbols)
s = int(nr_symbols)
n = int(nr_numbers)
wc = 0  # alphabet count
sc = 0  # symbol count
nc = 0  # numbers count
password = []
for num in range(0, nr_letters):
    x = random.randint(1, 3)
    if x == 1 and wc < w:
        password.append(letters[random.randint(0, 51)])
        wc += 1
    elif x == 2 and sc < s:
        password.append(symbols[random.randint(0, 7)])
        sc += 1
    elif x == 3 and nc < n:
        password.append(numbers[random.randint(0, 9)])
        nc += 1
    else:  
        password.append(letters[random.randint(0, 51)])
password = ''.join(password)
print(password)
