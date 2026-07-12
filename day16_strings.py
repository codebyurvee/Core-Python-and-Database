#String 
# sequence of characters within a '', "", ''' '''
# myString = "Hello Worlds"
# print(myString)

# # first index
# print(myString[0])
# # # # last index
# print(myString[-1])
# # # # sequence of string with skip a character
# print(myString[1:])
# print(myString[1:8:2])
# print(myString[-1:-5:-1])


# string escape sequences

# \n = next Line
# \t = tab(5 spaces)
# \b = remove one character from rightside
# \\ = \
# \" = "
# \' = '
# \r = home return(carriage)
#
# myString = "catat\rat"
# print(myString)
# myString = 'Hello \'Python\' Coders'
# print(myString)
# myString = '''Hello
#     Python
#         Coders'''
# print(myString)

# string escape sequences

# \n = next Line
# \t = tab(5 spaces)
# \b = remove one character from rightside
# \\ = \
# \" = "
# \' = '
# \r = home return(carriage)

# str = 'hello k\rworld'
# print(str)

# myString = "python Programming"
# print(myString.upper())
# myString = myString.lower()
# print(myString)
# print(myString.isupper())
# myString = myString.replace('Programming', 'Coders')
# print(myString)

# return index
# print(myString.find('n'))


# Split : split the string in list
# myString = "Amritsar is a beautiful city"
# # print(myString[0])
# # # #
# newList = myString.split(' ')
# print(newList)
# print(newList[0])


# myString = "chandigarh is a beautiful city"
# print(myString.islower())
# myString2 = " Hello"
# num = 10
# print(myString2+num)
# # # # error not possible string with int
# print(myString2+num)
# #
num1=10
num2=78
sum = num1+num2
# print('sum of ',num1,' and ',num2,'= ',sum)
# print(f'sum of {num1} and {num2} is {sum}')
# # # #
# data = 'sum of {0} and {1} is {2}'
# print(data.format(num1,num2, sum))
# #
# print("sum of {} and {} is {}".format(num1,num2, sum))

# myString = "Hello world you are beautiful"
# str2= myString.split(' ')
# print(str2)
# str1 = ' '.join(str2)
# print(str1)
# split, join, replace, islower, isupper , lower, upper, format, concat, find,len

#Indexing of a string 
stri = "hello Everyone"
print(stri[2:10:2])
print(stri[-2:-9:-1])
print(stri[::-1])
print(stri[-1:-10:-1])

#String Escape Squences
print("Hey\nEsha")
print("hey\tEsha")
print("Hello \"Python\"")
print("C:\\Users\\Isha")

#String Functions 
print(stri.upper())
print(stri.lower())
print(stri.replace("Everyone","Guys"))
print(stri.find("y"))
print(len(stri))

#Split joint
sentence = "I am Esha "
word = sentence.split(" ")
print(word)
new_sentence = "-".join(word)
print(new_sentence)

#Formatting 
name = "Esha"
age = 20
print(f"my name is {name}.I am {age} years")

#Mini Exercise 
Print the first, middle, and last character of "Artificial Intelligence".
Convert "Python" to uppercase and lowercase.
Replace "India" with "Japan" in "I live in India".
Count the length of "Machine Learning".
Split "Apple Mango Banana" into a list.
Join ["AI", "ML", "DL"] using "-".
Find the index of "g" in "Programming".
Print a sentence using an f-string
#Check if a string is palindrome
#remove all the vowels in a given string
#Reverse a string
#convert first letter of each word capital
#Convert string to uppercase and lowercase
# Count vowels in a string
# Reverse words in a sentence
# Replace spaces with underscores
#Find the length of a string without using len()
# Remove duplicate characters from a string
