import math
#1. The Walrus Operator :=
# Instead of calculating len() twice:
# if len(data) > 5: print(len(data))

if (n := len([1, 2, 3, 4, 5, 6])) > 5:
    print(f"List is too long with {n} elements")

#. Matrix Multiplication Operator (@)
# Used with libraries like NumPy or custom classes
# matrix_c = matrix_a @ matrix_b

#3. Bitwise Operators
a & b #and
a | b #or
a ^ b #xor
~a    #not 
a >> b #left shift
a << b #right shift

#QUESTIONS
# Write a program in Python to calculate simple interest?
def simpleintrest():
    i = 0
    p = int(input("enter amount: "))
    r = float(input("enter intrest rate: "))
    t = float(input("enter duration"))
    i = (p * r * t)/100
    print("simple intrest",i)
              
# Write a program in Python to calculate the area of a circle?
def circlearea():
    r = int(input("enter radius of circle : "))
    area = math.pi*r*r
    print("area of circle is",area)
    
# Write a program in Python to calculate the area of a square?
def squarearea():
    a = int(input("enter the side of square: "))
    area= a*a
    print("area of sqaure is",area)
    
# Write a program in Python to calculate the total number of marks and percentage of 5 subject
def marks():
    try:
        math = int(input("enter maths marks: "))
        english = int(input("enter english marks: "))
        hindi = int(input("enter hindi marks: "))
        science = int(input("enter science marks: "))
        punjabi = int(input("enter punjabi marks: "))
        total = math+english+hindi+science+punjabi
        print("your total marks is :",total)
 
        percentage = (total/500)*100
        print(percentage," is your toatal percentage in 500 marks")
    except ValueError:
        print("value error")    
    
# Write a program in Python to swap 2 numbers using 3 variables?
def swap():
    a = 3
    b = 5
    
    c = a
    a = b
    b = c
    print( " a was 3 and now",a)
    print(" b was 5 and now",b)
    
# Write a program to read a number in the dollar and convert it to INR?
def dollar_to_inr():
    dollar = float(input("United State Dollars: "))
    inr = dollar * 95.69
    print("Indian Rupee: ",inr)
    
# Write a program to calculate the volume of a cylinder
def c_volume():
    r = int(input("enter radius of cylinder: "))
    h = int(input("enter height of cylinder: "))
    volume = math.pi*r*r*h
    print("volume of cylinder is:",volume)


