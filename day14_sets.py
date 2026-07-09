# Set in Python
#
# Set is an unordered and unindexed collection of elements enclosed within{}
# Duplicates Values are not allowed in Set
# 
# s1 = {20,False,24.8,"Ram",0}
# print(s2)
#
# s1 = {True, 'a', 0,'Hello'}
# print(s1)

# = > Adding a new element
# s1.add("Hello Set")
# print(s1)
# // add randomly as Set is unindexed collection
# s1 = {1, 'a', True,'Hello'}
# print(s1)
#
# set1 = {"abc", 34, True,1, 40, "male"}
# # # # # #
# print(set1)

# = > Updating multiple elements
# set1.update({10, 20, 30})
# print(set1)
# s1 = {1, 'a', 10, 'Hello', 20, 30, True}
#
# = > Removing element
# s1.remove("a")
# print(s1)
# s1 = {1, True, 'Hello'}

# = > Union of two sets
# s1 = {1, 2, 3}
# s2 = {'a', 'b', 'c'}
# s3=s1.union(s2)
# print(s3)
# print(s1|s2)
# print({1, 2, 3, 'a', 'b', 'c'})
#
# = > intersection of two sets:
# s1 = {1, 2, 3, 4, 5, 6}
# s2 = {8,9,7,5,6,1}
# print(s1&s2)
# s3=s1.intersection(s2)
# print(s3)
# {1, 2, 5, 6}

# Removing multiple element
# s1 = {1, 2, 3, 4, 5, 6}
# rem_element = {4,5,6}
# del_element = s1.intersection(rem_element)
# s1-=del_element
# print(s1).


#PRACTICE OF SET
#Creation 
se = {'a',2,"hey","3.2"}
print(se)
print(type(se))

#adding element
se.add("esha")
print(se)
se = {"hi",3,6,5.5}
print(se)
se1 = {"a","bella","chikaksha","hey"}

#updating multiple values
se.update({23,"shinny"})
print(se)

#Remove Element 
se.remove("hi")
print(se)
 
#union of sets
se2 = se.union(se1)
print(se2)
print(se|se1)

#intersection of sets
se3 = se.intersection(se1)
print(se3)
print(se1&se)

#Removing multiple elements

