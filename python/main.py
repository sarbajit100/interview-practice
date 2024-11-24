# GENERATE AN INFINITE FIBONNACI RERIES BY GENERATER

# def fibonacci():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# f1 = fibonacci()
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))

# l = [1,2,8,6,25,88,21,4]

# n = len(l)

# for i in range(n):
#     for j in range(i+1,n):
#         if l[i]>l[j]:
#             l[i],l[j] = l[j],l[i]
            
# print(l)

# check a string is palidrom or not

# s = "jaaj"
# n = len(s)
# x=0
# for i in range(n):
#     if s[i] != s[n-i-1]:
#         x=1
        
# if x==0:
#     print(s, "is a palidrom")
# else:
#     print(s, "is not a palidrom")

# s = "jaaj"

# if s == s[::-1]:
#     print(s, "is a pallindrom")
# else:
#     print(s, "is not a pallindrom")

# short a dictionary

# dic = {1:5, 5:3, 2:9, 8:1}

# result = {k:v for k,v in sorted(dic.items(), key = lambda item:item[0])}
# print(result)
# dic2 = {}
# items = dic.keys()
# sorted_keys = sorted(items)
# for i in sorted_keys:
#     dic2[i] = dic[i]
# print(dic2)

# dic = {1:5, 5:3, 2:9, 8:1}

# result = {k:v for k,v in sorted(dic.items(), key = lambda item:item[1])}
# print(result)
# dic2 = {}
# values = dic.values()
# sorted_values = sorted(values)
# keys = dic.keys()

# for i, j in zip(sorted_values, keys):
#     dic2[j] = i

# print(dic2)

# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.


# Complete the solve function below.
# def solve(s):
#     for name in s.split():
#         s=s.replace(name, name.capitalize())
#     return s
    
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = solve(s)

#     fptr.write(result + '\n')

#     fptr.close()

# s= "abcabcdbb"
# char_set = set()
# longest_sub_string = ""
# left = 0
# max_length = 0
# for right in range(len(s)):
#     while s[right] in char_set:
#         char_set.remove(s[left])
#         left += 1
#     char_set.add(s[right])
#     if right - left + 1 > max_length:
#         max_length = right - left + 1
#         longest_sub_string = s[left:right + 1]
    
    
# print(f"Longest sub string is: '{longest_sub_string}'it has: '{max_length}' character")

# if right - left + 1 > max_length:
#         max_length = right - left + 1
#         longest_sub_string = s[left:right + 1]


# s= "abcabkkjjjjjcdbb"
# my_set = set(s)

# my_dict = {}

# for i in range(len(s)-1):
#     if s[i] in my_set:
#         my_dict[s[i]] = my_dict.get(s[i], 0) +1
        
# for i in range(len(s)):
    
#     if s[i] not in my_dict:
#         my_dict[s[i]] = 1
#     else:
        
#         my_dict[s[i]] += 1
        
# print(my_dict)

# def longest_string_between_duplicates(s):
#     # Remove spaces from the string
#     s = s.replace(" ", "")  # or use s = ''.join(s.split())
    
#     # Dictionary to store the first occurrence index of each character
#     char_indices = {}
#     longest_substring = ""
    
#     # Traverse the string using a for loop with range
#     for i in range(len(s)):
#         char = s[i]
#         if char in char_indices:
#             # If character already seen, calculate the substring between first and second occurrence
#             start_index = char_indices[char] + 1
#             substring = s[start_index:i]
            
#             # Update the longest substring if the current one is longer
#             if len(substring) > len(longest_substring):
#                 longest_substring = substring
#         else:
#             # Store the index of the first occurrence of the character
#             char_indices[char] = i
    
#     return longest_substring

# # Example usage:
# input_string = "abc de ffg hijklmnoab cxyz"
# longest_substring = longest_string_between_duplicates(input_string)
# print(f"Longest substring between duplicate characters: '{longest_substring}'")


# ____________________________________________________________________________________

# def longest_string_between_duplicates(s):
#     # Dictionary to store the first occurrence index of each character
#     s = s.replace(" ", "")
#     char_indices = {}
#     longest_substring = ""
    
#     # Traverse the string
#     for i, char in enumerate(s):
#         if char in char_indices:
#             # If character already seen, calculate the substring between first and second occurrence
#             start_index = char_indices[char] + 1
#             substring = s[start_index:i]
            
#             # Update the longest substring if the current one is longer
#             if len(substring) > len(longest_substring):
#                 longest_substring = substring
#         else:
#             # Store the index of the first occurrence of the character
#             char_indices[char] = i
    
#     return longest_substring

# # Example usage:
# input_string = "This is a demo for testing duplicate demo"
# longest_substring = longest_string_between_duplicates(input_string)
# print(f"Longest substring between duplicate characters: '{longest_substring}'")


# def shortest_substring_between_duplicates(s):
#     min_length = len(s) + 1
#     start_index = -1
#     end_index = -1

#     for i in range(len(s)):
#         for j in range(i + 1, len(s)):
#             # Check if there's a duplicate character
#             if s[i] == s[j]:
#                 # Calculate the length between duplicates
#                 length = j - i - 1
                
#                 # Update minimum length and substring indices if this is the shortest found
#                 if length < min_length:
#                     min_length = length
#                     start_index = i + 1
#                     end_index = j
#                 break  # Stop once we find the next duplicate for this character

#     # Manually build the substring between start_index and end_index
#     result = ""
#     if start_index != -1 and end_index != -1:
#         for k in range(start_index, end_index):
#             result += s[k]

#     return result if result else "No duplicate characters found"

# # Test example
# s = "abcdae"
# print("Shortest substring between duplicates:", shortest_substring_between_duplicates(s))


# def shortest_substring_between_duplicates(s):
#     char_indices = {}
#     min_length = float('inf')
#     shortest_substring = ""

#     for i, char in enumerate(s):
#         # If the character is seen before
#         if char in char_indices:
#             # Calculate the distance between the duplicates
#             start_index = char_indices[char]
#             length = i - start_index - 1  # Exclude the duplicate characters themselves
            
#             # Update the minimum length and substring if this is the shortest
#             if length < min_length:
#                 min_length = length
#                 shortest_substring = s[start_index + 1 : i]
#         # Store the index of the first occurrence of the character
#         char_indices[char] = i

#     # Return the result or indicate if no duplicate characters were found
#     return shortest_substring if shortest_substring else "No duplicate characters found"

# # Test example
# s = "abcdae"
# print("Shortest substring between duplicates:", shortest_substring_between_duplicates(s))


# 1.X = [10,20,30] print last 2 values using : operator

# X = [10,20,30]
# print(X[-2:])

# 2.X = [10,20,30] print all elements using : operator

# X = [10,20,30]
# print(X[0:])

# 3.X = [10,20,30,40…100] print 10 30 50 and so on (alternative elements) without using the for loop.
# Hint - use :: operator

# X = [10,20,30,40,50,60,70,80,90,100]
# print(X[::2])

# 4.Store 10,20,30,....980,990,1000 into a list. Hint - use range

# numbers = list(range(10, 1001, 10))
# print(numbers)

# 5.Take a list of 10 elements print elements in reverse order, hint use :: operator

# x=[1,2,3,4,5,6,7,8,9,10]
# print(x[::-1])

# 6.Take a list of 10 elements print elements in reverse order using for loop

# x=[1,2,3,4,5,6,7,8,9,10]
# for i in range(len(x)-1,-1,-1):
#     print(x[i])

# 7.Take a list of 10 elements print all elements using for loop

# x=[1,2,3,4,5,6,7,8,9,10]
# for i in range(0,len(x)):
#     print(x[i])

# 8.Show one eg for the property list is mutable

# my_list = [1, 2, 3, 4, 5]
# print("Original list:", my_list)
# my_list[1] = 20
# print("Modified list:", my_list)

# 9.Modify 2nd index element of list with 300

# my_list = [1, 2, 3, 4, 5]
# my_list[1] = 300
# print(my_list)

# 10.Which method do you use to search if a given element is available in the list. Show e.g.
# how do you use it. What happens if the element is not available?

# Sample list
# my_list = [10, 20, 30, 40, 50]

# element1 = 30

# Check if the element is in the list
# if element1 in my_list:
#     print(f"{element1} is in the list.")

# Check if the element is in the list by index

# element2=31
#
# index = my_list.index(element2)
# print(f"{element2} is in the list at index {index}.")
# ValueError: 31 is not in list

# 11. Which method do you use to delete an element present in the list. Show one e.g. how do you use it.

# my_list = [10, 20, 30, 40, 50]
# element = 10
# my_list.remove(element)
# print(my_list)

# 12. Insert a new element before 1st index in the list using a method of list, show e.g. of that method

# my_list = [10, 20, 30, 40, 50]
# new_element = 6
# my_list.insert(0, new_element)
# print(my_list)

# 13. Which method do you use to delete an element present in the 1st index of the list? Show code.

# my_list = [10, 20, 30, 40, 50]
# removed_element = my_list.pop()
# print(f"Removed element: {removed_element}")
# print(my_list)

# 14.x=[ (10,20), (30,40), (50,60) ] print element 40

# x = [(10, 20), (30, 40), (50, 60)]
# print(x[1][1])

# 15. In the above example what will happen if we print(x[-1][-1])
# 60

# *******************************************_____ SET _____***********************************

# 1. Create an empty set.

# x = set()
# print(type(x))

# 2. Store 10,20,30 in a set and print 10 using index

# Sets in Python are unordered collections, meaning they do not support indexing like lists or tuples. Therefore, you
# can't access elements of a set using an index.

# 3.Print set elements using for loop

# x = {1, 2, 3, 4, 9, 8, 7, 8}
# for i in x:
#     print(i)

# 4. Set stores elements in insertion order [t/f]
# False

# 5. Sets are faster compared to lists [t/f]
# True

# 6.Which method do you use to add a new element into the set? Show eg

# x = {1, 2, 3, 4, 9, 8, 7, 8}
# x.update([40, 50, 60])
# x.add(20)
# print(x)

# 7.Which method do you use to delete an element from a set? Show eg

# x = {1, 2, 3, 4, 9, 8, 7, 8}
# x.update([40, 50, 60])
# x.discard(60)
# x.remove(3)
# print(x)

# ************************************************   Dictionary   *********************************************

# 1. Dictionary - Take a dictionary insert a new pair k=30

# d = {"a": 2, "b": 20}
# d.update(k=30)
# print(d)

# 2. Dictionary - Print the value of key i

# d = {"a": 2, "b": 20, "i": 40}
# print(d["i"])

# 3. Dictionary - In the dictionary update value of key j with 20

# d = {"a": 2, "b": 20, "j": 40}
# d["j"] = 20
# print(d)

# 4. Dictionary x = {‘i’:10, ‘i’ : 20 } what happens if i print (x)
# SyntaxError

# 5.Dictionary - does it allow duplicate values
# True

# 6. Dictionary - can we get key based on value? Why?

# my_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
# value_to_find = 'c'
# key = None
# for k, v in my_dict.items():
#     if v == value_to_find:
#         key = k
#         break
# print(key)

# 7. Dictionary - print(x[‘i’]) assume that key i is not available, what happens?
# SyntaxError

# 8. Print dictionary keys and values using a for loop.

# my_dict = {1: 'apple', 2: 'banana', 3: 'cherry', 4: 'date'}
# for key, value in my_dict.items():
#     print(f"Key: {key}, Value: {value}")

# 9. How will you print only keys present in the dictionary?

# my_dict = {1: 'apple', 2: 'banana', 3: 'cherry', 4: 'date'}
# for key in my_dict.keys():
#     print(f"Key: {key}")

# 10. How will you print only values present in the dictionary?

# my_dict = {1: 'apple', 2: 'banana', 3: 'cherry', 4: 'date'}
# for value in my_dict.values():
#     print(f"Value: {value}")

# 11.Which method of dictionary do you use to find if a given key is available in the dictionary or not? Show eg .

# my_dict = {1: 'apple', 2: 'banana', 3: 'cherry', 4: 'date'}
#
# if 6 in my_dict:
#     print("key is available")
# else:
#     print("key is not available")

# 12. Which method do you use to get the value of a given key from a dictionary? Show eg?

# my_dict = {1: 'apple', 2: 'banana', 3: 'cherry', 4: 'date'}
# key = 2
# value = my_dict.get(2)
# print(f"Key: {2} value: {value}")

# 13. Which method do you use to delete a pair from the dictionary based on the given key. Show eg

# my_dict = {1: 'apple', 2: 'banana', 3: 'cherry', 4: 'date'}
# key_to_delete = 2
# value = my_dict.pop(key_to_delete)
# print(f"Removed value: {value}")
# print(f"Modified dictionary: {my_dict}")

# 14. X = { ‘i’ : [10,20], ‘j’:[40,50] } print 10,20

# x = {"i": [10, 20], "j": [40, 50]}
# y = x.get("i")
# print(y[0], y[1])

# 15. X = { ‘i’ : [10,20], ‘j’:[40,50] } print 20

# x = {"i": [10, 20], "j": [40, 50]}
# y = x.get("i")
# print(y[1])

# 16. X = { ‘i’ : [10,20], ‘j’:[40,50] } print 50

# x = {"i": [10, 20], "j": [40, 50]}
# y = x.get("j")
# print(y[1])

# 17. X = { ‘a’: {‘i’:10, ‘j’:20}, ‘b’:{‘i’:100, ‘j’:200} } print 10

# x = {"a": {"i": 10, "j": 20}, "b": {"i": 100, "j": 200}}
# y = x.get("a")
# z = y.get("i")
# print(z)

# 18. X = { ‘a’: {‘i’:10, ‘j’:20}, ‘b’:{‘i’:100, ‘j’:200} } print 200

# x = {"a": {"i": 10, "j": 20}, "b": {"i": 100, "j": 200}}
# y = x.get("b")
# z = y.get("j")
# print(z)

# 19. X = { ‘a’: {‘i’:10, ‘j’:20}, ‘b’:{‘i’:100, ‘j’:200} } dictionary a present in dictionary x

# x = {"a": {"i": 10, "j": 20}, "b": {"i": 100, "j": 200}}
# y = x.get("a")
# print(y)

# ********************************************  Functions default arg kwargs parameters ***************************

# 1. Trainer can ask find output based questions on default parameters

# def greet(name, message="Hello"):
#  return f"{message}, {name}!"
#
# print(greet("Alice"))
# print(greet("Bob", "Hi"))
# print(greet("Charlie", message="Good morning"))

# 2. Trainer can ask how do you call this method (with default parameter)

# 3. What is the data type of args internally

# The *args syntax allows the function to accept any number of positional arguments.
# These arguments are collected into a tuple named args.

# 4. What is the data type of kwargs internally

# The **kwargs syntax allows the function to accept any number of keyword arguments.
# These arguments are collected into a dictionary named kwargs.

# 5. How many times can we use args for a given function?

# In a given function definition, you can only use *args once.
# The *args parameter allows the function to accept a variable number of positional arguments, and having more than one such parameter would make it ambiguous as to which arguments belong to which *args parameter. Here is the rule and an example to clarify:

# Rule:
# A function can have only one *args parameter.
# You can, however, have other parameters before and after *args, including regular positional parameters, keyword parameters, and **kwargs.

# 6. How many times can we use kwargs for a given function?


# In a given function definition, you can only use **kwargs once. The **kwargs parameter allows the function to accept a variable number of keyword arguments, and having more than one such parameter would cause ambiguity and is not allowed by Python's syntax rules.
#
# Rule:
# A function can have only one **kwargs parameter.
# You can combine **kwargs with other parameters such as regular positional parameters, default parameters, and *args.

# 7. How many default parameters can we use for a given function?


# In Python, there is no fixed limit on the number of default parameters you can use in a given function. You can define as many default parameters as you need. However, default parameters must be placed after any positional parameters and before any *args or **kwargs in the function definition. Here's a summary of the parameter order and an example with multiple default parameters:

# 8. Def f1(a,b,*c,d=10,**e) : pass call this method and pass 1 to a, 2 to b, 3,4,5 to c and 6
# to d and pass hno=10 street =btm to e.

# def f1(a, b, *c, d=10, **e):
#  print(f"a: {a}")
#  print(f"b: {b}")
#  print(f"c: {c}")
#  print(f"d: {d}")
#  print(f"e: {e}")

# f1(1, 2, 3, 4, 5, d=6, hno=10, street='btm')

# 9. Def f1(x,y,*z=10): pass what happens if we call f1(10) what will be x y z values

# syntax error

# 10. Def f1(x,y,*z=10): pass what happens if we call f1(10,20,30) what will be x y z values

# x: 10
# y: 20
# z: (30,)

# **********************************************   List comprehension:   *****************************************

# 1. Take a list l1 copy all l1 elements into l2

# Using Slice Operator
# l1 = [1, 2, 3, 4, 5]
# # Using Slice Operator
# l2 = l1[:]
# # Using copy() method
# l3 = l2.copy()

# print("l1:", l1)  # Output: l1: [1, 2, 3, 4, 5]
# print("l2:", l2)  # Output: l2: [1, 2, 3, 4, 5]
# print("l3:", l3)  # Output: l2: [1, 2, 3, 4, 5]

# 2. Take a list l1 copy double of each element of l1 into l2

# l1 = [1, 2, 3, 4, 5]
# l2 = [x * 2 for x in l1]

# print("l1:", l1)  # Output: l1: [1, 2, 3, 4, 5]
# print("l2:", l2)  # Output: l2: [2, 4, 6, 8, 10]

# 3. Take a list l1 copy each element power 2 of l1 into l2

# l1 = [1, 2, 3, 4, 5]
# l2 = [x ** 2 for x in l1]

# print("l1:", l1)  # Output: l1: [1, 2, 3, 4, 5]
# print("l2:", l2)  # Output: l2: [2, 4, 6, 8, 10]

# 4. Take a list l1 copy each element+1 into l2

# l1 = [1, 2, 3, 4, 5]
# l2 = [x + 1 for x in l1]

# print("l1:", l1)  # Output: l1: [1, 2, 3, 4, 5]
# print("l2:", l2)  # Output: l2: [2, 4, 6, 8, 10]

# 5. Take a list l1 copy all even numbers into l2

# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# l2 = [number for number in l1 if number % 2 == 0]

# print(l2)

# 6. Take name=’palle’ copy all letters into l2 if it is not vowel

# name = "palle"
# vowel=["a", "e", "i", "o", "u"]
# l2 = [i for i in name if i in vowel]
#
# print(l2)

# 7. Copy even numbers from 0 to 11 into a list using comprehension

# Using list comprehension to get even numbers from 0 to 11

# l2 = [number for number in range(12) if number % 2 == 0]
#
# # l2 now contains all the even numbers from 0 to 11
# print(l2)

# ********************************  Lambda expression   *****************************************

# 1. Write a lambda expression which takes one parameter and returns element power 2, call
# that function and print the returned value

# square = lambda x: x ** 2
# result = square(5)
# print(result)

# 2. Write a lambda expression which takes 3 parameters and returns a sum. Call and print.

# sum_three = lambda a, b, c: a + b + c
# result = sum_three(3, 5, 7)
# print(result)

# 3. Write a lambda expression to find the biggest of 2 numbers. Call and print

# max_of_two = lambda a, b: a if a > b else b
# result = max_of_two(10, 20)
# print(result)

# 4. Take a list l1 copy each element+1 into l2 using map() function

# l1 = [1, 2, 3, 4, 5]
# l2 = list(map(lambda x: x + 1, l1))
# print(l2)

# 5. Take a list l1 copy all even numbers into l2 using filter() function

# l1 = [1, 2, 3, 4, 5]
# l2 = list(filter(lambda x: x%2 == 0, l1))
# print(l2)

# 6. Take a list l1 copy all elements which are greater than 10 into l2 using filter function

# l1 = [1, 2, 3, 4, 5, 10, 16, 19]
# l2 = list(filter(lambda x: x>10, l1))
# print(l2)

# 7. Take a list l1 copy half of each element into l2 using map() function

# l1 = [1, 2, 3, 4, 5, 10, 16, 19]
# l2 = list(filter(lambda x: x>10, l1))
# print(l2)

# 8. Take a list l1 copy all odd numbers into l2 using filter() function

# l1 = [1, 2, 3, 4, 5]
# l2 = list(filter(lambda x: x%2 != 0, l1))
# print(l2)

# ***************************************    Class & object:    *****************************************

# 1. Trainer can ask to call methods of a class with object

# 2. Trainer can ask to create a class with some requirements like mentioned in the
# constructor's first question. Trainer has to elaborate the requirements properly.
# Eg: create a patient class and create 2 patient objects with values pno=1,
# pname=ramesh, disease = fever. pno=2, pname=suresh, disease=cold.
# This requires students to create init method also with appropriate parameters. (this
# question can be included in constructor also)

# class Patient:
#     def __init__(self, pno, pname, disease):
#         self.pno = pno
#         self.pname = pname
#         self.disease = disease
#
#     def display_info(self):
#         print(f"Patient No: {self.pno}")
#         print(f"Patient Name: {self.pname}")
#         print(f"Disease: {self.disease}")
#
# # Creating the patient objects with the specified values
#
# patient1 = Patient(1, "Ramesh", "Fever")
#
# patient2 = Patient(2, "Suresh", "Cold")
#
# # Displaying the information of each patient
# patient1.display_info()
# print()  # Just to add a line break between the outputs
# patient2.display_info()


# *************************************    Constructor:    ***************************************

# 1. There are 2 students with values sno-1 sname-ramesh sub-python, sno-2 snake=suresh
# sub AI. create a student class with init() and display(). Create above 2 objects and print
# each student object values by calling display() function

# class Student:
#     def __init__(self, sno, sname, sub):
#         self.sno = sno
#         self.sname = sname
#         self.sub = sub
#
#     def display_info(self):
#         print(f"Patient No: {self.sno}")
#         print(f"Patient Name: {self.sname}")
#         print(f"Disease: {self.sub}")
#
# # Creating the patient objects with the specified values
#
# student1 = Student(1, "Ramesh", "python")
# student2 = Student(2, "Suresh", "AI")

# # Displaying the information of each patient
# student1.display_info()
# print()  # Just to add a line break between the outputs
# student2.display_info()

# 2. Same as above question, print student object values with object without calling display()

# class Student:
#     def __init__(self, sno, sname, sub):
#         self.sno = sno
#         self.sname = sname
#         self.sub = sub
#
# student1 = Student(1, "Ramesh", "python")
# student2 = Student(2, "Suresh", "AI")
# print(student1.sno, student1.sname, student1.sub)
# print(student2.sno, student2.sname, student2.sub)

# 3. Calling constructor with parameter, correct way to create object for that class. Trainer
# should ask the code based question on this.

# 4. Can we remove self parameter from init

# False

# 5. Can we place x in place of self parameter in init

# True but not recommended

# 6. Can I overload constructor? What will happen if we overload constructor?

# class Patient:
#     def __init__(self, *args):
#         if len(args) == 3:
#             self.pno = args[0]
#             self.pname = args[1]
#             self.disease = args[2]
#         elif len(args) == 2:
#             self.pno = args[0]
#             self.pname = args[1]
#             self.disease = None
#         elif len(args) == 1:
#             self.pno = args[0]
#             self.pname = None
#             self.disease = None
#         else:
#             self.pno = None
#             self.pname = None
#             self.disease = None
#
#     def display_info(self):
#         print(f"Patient No: {self.pno}")
#         print(f"Patient Name: {self.pname}")
#         print(f"Disease: {self.disease}")
#
# # Creating patient objects with different initialization scenarios
# patient1 = Patient(1, "Ramesh", "Fever")
# patient2 = Patient(2, "Suresh")
# patient3 = Patient(3)
# patient4 = Patient()

# # Displaying the information of each patient
# patient1.display_info()
# print()  # Just to add a line break between the outputs
# patient2.display_info()
# print()  # Just to add a line break between the outputs
# patient3.display_info()
# print()  # Just to add a line break between the outputs
# patient4.display_info()


# class Patient:
#     def __init__(self, *args):
#         if len(args) == 3:
#             self.pno = args[0]
#             self.pname = args[1]
#             self.disease = args[2]
#         elif len(args) == 2:
#             self.pno = args[0]
#             self.pname = args[1]
#             self.disease = None
#         elif len(args) == 1:
#             self.pno = args[0]
#             self.pname = None
#             self.disease = None
#         else:
#             self.pno = None
#             self.pname = None
#             self.disease = None
#
#     def display_info(self):
#         print(f"Patient No: {self.pno}")
#         print(f"Patient Name: {self.pname}")
#         print(f"Disease: {self.disease}")
#
# # Creating patient objects with different initialization scenarios
# patient1 = Patient(1, "Ramesh", "Fever")
# patient2 = Patient(2, "Suresh")
# patient3 = Patient(3)
# patient4 = Patient()
#
# # Displaying the information of each patient
# patient1.display_info()
# print()  # Just to add a line break between the outputs
# patient2.display_info()
# print()  # Just to add a line break between the outputs
# patient3.display_info()
# print()  # Just to add a line break between the outputs
# patient4.display_info()


# 7. Can we create object without calling constructor

# You can use object.__new__ to create an instance without invoking the __init__ method.
# This method is lower-level and is used to allocate memory for a new instance without initializing it.

# class Patient:
#     def __init__(self, pno, pname, disease):
#         print("Initializing...")
#         self.pno = pno
#         self.pname = pname
#         self.disease = disease
#
#     def display_info(self):
#         print(f"Patient No: {self.pno}")
#         print(f"Patient Name: {self.pname}")
#         print(f"Disease: {self.disease}")
#
# # Create an object without calling the __init__ method
# patient = object.__new__(Patient)
#
# # Manually setting attributes
# patient.pno = 1
# patient.pname = "Ramesh"
# patient.disease = "Fever"
#
# # Displaying the information of the patient
# patient.display_info()


# 8. What is the sequence of object creation and constructor call?

# In Python, the sequence of object creation and constructor call involves several steps,
# primarily handled by two special methods: __new__ and __init__. Here's a detailed explanation of the sequence:
# 
# Sequence of Object Creation and Constructor Call
# Object Creation (__new__ method):
# 
# The __new__ method is the first step in the object creation process.
# It is responsible for creating a new instance of the class.
# __new__ is a static method that takes the class as its first argument,
# followed by any additional arguments that will be passed to the __init__ method.
# __new__ returns a new instance of the class.
# Object Initialization (__init__ method):
# 
# After __new__ creates the instance, the __init__ method is called to initialize the instance.
# __init__ is an instance method that takes the newly created instance as its first argument (conventionally named self),
# followed by any additional arguments passed to the constructor.
# __init__ does not return anything; it modifies the instance in place.
class MyClass:
    def __new__(cls, *args, **kwargs):
        print("Creating instance (calling __new__)")
        instance = super().__new__(cls)
        return instance

    def __init__(self, value):
        print("Initializing instance (calling __init__)")
        self.value = value

    def display_value(self):
        print(f"Value: {self.value}")

# Creating an instance of MyClass
obj = MyClass(10)

# Displaying the value
obj.display_value()

# 9. Can we call a constructor after creating an object?

# In Python, the constructor (__init__ method) is called automatically when a new instance of a class is created.
# Once an object is created, calling the constructor directly in the same way as during object creation is not possible.
# However, there are a few ways to achieve similar functionality:

# class MyClass:
#     def __init__(self, value):
#         print("Initializing instance")
#         self.value = value
#
#     def display_value(self):
#         print(f"Value: {self.value}")
#
# # Creating an instance of MyClass
# obj = MyClass(10)
# obj.display_value()
#
# # Reinitializing the same instance
# obj.__init__(20)
# obj.display_value()


# 10. For one object how many times will the constructor be called? Can we call a constructor multiple times for one object?

# In Python, the constructor (__init__ method) is called automatically when an object is created.
# For one object, the constructor is called exactly once during the object's creation.
# Once the object has been created, the constructor is not called again automatically for that object.
# However, you can manually call the __init__ method on an existing object,
# but this is not the same as creating the object again; it is just a method call that can reinitialize the object's attributes.

# 11. Is it mandatory for every class to have constructor

# No, it is not mandatory for every class to have a constructor (__init__ method) in Python.
# If you don't explicitly define a constructor in your class, Python provides a default constructor for you.
# Default Constructor
# If you don't define a constructor in your class, Python automatically provides a default constructor.
# This default constructor doesn't do anything beyond what's necessary to create an instance of the class.

# 12. If we create 10 objects for a class, how many times will the constructor be called?

# If you create 10 objects for a class in Python, the constructor (__init__ method) will be called exactly 10 times,
# once for each object being created.

# class MyClass:
#     def __init__(self, value):
#         print("Constructor called with value:", value)
#         self.value = value
#
# # Creating 10 objects of MyClass
# objects = [MyClass(i) for i in range(10)]













































    