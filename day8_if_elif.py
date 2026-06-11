

# Question 1: Check if a number is positive, and if yes, check whether it is even or odd.
def numcheck():
  num = int(input("Enter a number: "))
  if num > 0:
    if num%2==0:
      print(num," is positive and it is an even number")
    else:
      print(num, " is positive and it is an odd number")
  elif num <0:
    print("it is negative number")
  elif num == 0:
    print("ur number is ", num)
  

#Question 2:Check whether a person is eligible to vote and also check if they are a senior citizen (age ≥ 60).
def agecheck():
  age = int(input("enter age :"))
  if age >= 18 and age<=60:
    print("eligible for vote")
  elif age >= 60:
    print("you are senior citizen and u can vote")
    
#Question 3:Check if a number is zero. If not, check whether it is positive or negative.
def check_zero():
  num = int(input("enter a number"))
  if num == 0 :
    print("it is zero")
  elif num >0:
    print("positive")
  elif num<0:
    print("negative")


#Question 4:Check login using nested if

def login():
  admin = "Esha"
  passw = 1234
  ad = input("Enter admin user-id: ")
  ps = int(input("enter your 4 digit password: "))
  if ad ==admin:
    if ps == passw:
      print("you are logged in")
    else:
      print("invailed password")
  else:
    print("invailed user id")


'''Question 5: Take age & weight and check
             if age is greater than equal 18
             if weight is greater than equals 55
   if both above condition satisfied then
         print candidate can donate blood
         otherwise not'''

def age_w():
  age = int(input("enter your age: "))
  weight = int(input("enter your weight: "))
  if age >= 18  and weight >=55:
    print("you are eligible to donate blood")
  else:
    print("u r not eligible to donate blood")

