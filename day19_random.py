import random as ra
print(ra.random())
print(ra.randint(1,6)) #dice
print(ra.randrange(1,10,2))
fruits = ["apple","Mango","litchi"]
print(ra.choice(fruits))
nums = [23,57,87,56,98,14]
ra.shuffle(nums)
print(nums)

#Lets make some games 
#1.dice
print("1. DICE ROLLER")
print(ra.randint(1,6))

#2.coin toss
print("2. Coin Toss")
coin= ["Heads","Tails"]
print(ra.choice(coin))

#3.Guess the Number
print("3. GUESS THE NUMBER 1-10")
gn = ra.randint(1,10)

#4 password generation
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$&"
password = ""
for i in range(8):
    password += ra.choice(chars)
print(password)

#5. card suffule 

#6.otp generation
print(ra.randint(1111,9999))
