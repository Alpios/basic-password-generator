letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
import random
print("Welcome to the password generator!\n")
input_letter=int(input("How many letters would you like in your password? :"))
input_number=int(input("How many numbers would you like in your password? :"))
input_symbol=int(input("How many symbols would you like in your password? :"))

password1=[]
for i in range(input_letter):
    password1 += random.choice(letters)
for i in range(input_number):
    password1 += random.choice(numbers)
for i in range(input_symbol):
    password1 += random.choice(symbols)
random.shuffle(password1)
password=""
for i in password1:
    password+=i
print("Your password is:",password)