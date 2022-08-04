#importing random module
import random

#storing all the letters, symbols and numbers in different lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#start of the program
print("Welcome to the PyPassword Generator!")

#taking all required inputs to generate the password
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

"""
#Easy way - order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
random_pwd = ''
for letter in range(nr_letters):
  random_pwd += (random.choice(letters))
for symbol in range(nr_symbols):
  random_pwd += (random.choice(symbols))
for number in range(nr_numbers):  
  random_pwd += (random.choice(numbers))
print(random_pwd)
"""

#Hard Level - order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []
for letter in range(nr_letters):
  password_list += (random.choice(letters))
for symbol in range(nr_symbols):
  password_list += (random.choice(symbols))
for number in range(nr_numbers):
  password_list += (random.choice(numbers))


#shuffling the list elements to generate the random password
random.shuffle(password_list)
#print(password_list)

#converting this randomly shuffled list into a string
password = ''
for ch in password_list:
  password += ch

#printing the final password
print(f"Your password is {password}")
