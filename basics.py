#using variable and \n (escape command for next para)

# character_name = "abdul"
# character_age = "21"
# print("There once a man named " +character_name+ ".\n"
#       "His age is " +character_age+ " years old.\n"
#       "He really likes his name " +character_name+"\n"
#       "but dont like to be " +character_age+ " years old.")

# print("     / |")
# print("    /  |")
# print("   /   |")
# print("  /____|")

# phrase = "Arif ansari is a boy."
# is_male = phrase.startswith("A")
# print(is_male)
#
# is_male = True
# print(is_male)

#Concatenation
# phrase = "Hello World"
# print(phrase+ " in advance.")

# phrase = "grEy wolf"
# print(phrase.upper().isupper())
# print(len(phrase))
# print(phrase[6])
# print(phrase[:5])
# print(phrase.index('w'))
# print(phrase.find('o'))
# print(phrase.rfind('o'))
# print(phrase.replace("E","e"))

#basic calculator using float()
# num1 = float(input("Enter a number: "))
# num2 = float(input("enter another number:"))
# result = num1 + num2
# print(result)

#Creating Mad libs games
# moon = input("antonym of sun:")
# stars = input("moon is a:")
# wind = input("another word of air :")
# man = input("antonym of woman:")
# riding = input("another word of cycling:")
# late = input("another word of delay:")
# out = input("opposite of in:")
#
# print("whenever the "+ moon +" and "+stars+" are set,")
# print("whenever the " + wind + " is high,")
# print("A " + man + " goes " + riding + " by..")
# print(late + " in the night when the fires are " + out),
# print("why does he gallop and gallops about?")

#LISTS

# friends = ("abdul"," sufiyan "," hassan "," arman ", " imam")
# print(friends[-2:4])
# print(len(friends))
# print(friends.index("abdul"))
# print(friends.count("abdul"))
#
# list[start,stop,step]
# it does not include the stop value (or functions as an open bracket)
# nums = [42,5,9,18,1,7,9,91]
# print(nums[-5:-1:2])

# python itself gives you information about its 11 lists of method that it contains by using the following code
# print([method for method in dir(list)if not method.startswith('__')])

#append() and copy()
# num = [1,2,3,4,5,6,4j,7,8,9,True,False,5.9,]
# friends = ["Abdul"," sufiyan "," Hassan ","arman"]
# friends1 = friends.copy()
# num.append(99)
# friends.append("imam")
# print(friends)
# print(num)

# insert() + remove() + pop()
# num.insert(10,100)
# friends.insert(2,"sayeed")
#num.remove(4j)
#friends.remove(" Hassan ")
#print(num)
#print(friends)
#num.pop()
#print(num)

#extend() + concatenation of lists
#mates = ["khan imam salahuddin"]
#num.extend(friends + mates)
#print(num)

#index() and count()
# ==> always keep one thing in mind that in python whenever you write an item then its punctuations
#and all its spaces, everything matters as you can see different in results between " hassan " and "hassan".
#
# print(friends.index(" hassan "))
# print(friends.count(" sufiyan "))
# print(num.index(0))
# print(num.count(True))
#print(friends.index("hassan"))

#clear() and sort() + reverse()
#friends.clear()
#friends.sort()
#print(friends)
#num.clear()
#num.sort()  ===>> not supported between instances of 'complex' , 'int' and 'str'
#print(num)
# friends.reverse()
# print(friends)

#TUPLES
# ==>> it can store int, CN , str and boolean values and are faster than lists
# coordinates = (5,6,9)
# coordinates.reverse()
# print(coordinates)    ==>>tuples are similar to lists but are immutable(unchangeable)
# my_tuples = (5,6,"amir",4j,0,True,1)
# print(my_tuples[4])
# my_tuples[1] = "hassan"  ==> if my_tuples are list..
# print(my_tuples)

#FUNCTIONS
# def greet(name, age):
#     print("Hello, " + name + " you're "+ str(age)+"!")
# greet("Arif","20")
# greet("Abdul","19")
#
# def customer(name):
#     print(f"Hello, {name}! you're welcome..")
# customer("Arif")
#
# def greeting(name= "guest"):
#     return f"Hello {name}!"
# print(greeting())
# print(greeting("Arif"))
#
# def add(a,b):
#     return a+b
# result = add(1,2)
# print(result)


# def I_am(name = "Guest"):
#     print(f"Hello {name}! you are welcome here..")
# (I_am("sara"))
#
# def I_am(name = "Guest"):
#     return f"Hello {name}! you are welcome here.."
# print(I_am("neha"))

# def example():
#     print("line 1")
#     return 5
#     print("line 2")
# print(example())

#LAMBDA FUNCTION
#usually we do this :-
# def multiply(x,y):
#     return x * y
# print(multiply(2,5))

#but using lambda function we can actually short it up.
# mult = lambda x,y : x*y
# result = mult(2,5)
# print(result)

#we will understand it by another example is None:
# nums = [1,2,3,4,5,6,7,8,9]
# def double(x):
#     return x * 2
# result = map(double, nums)
# print(list(result))
# A 5 lines code

# Now let's do it by using lambda function
# nums = [1,2,3,4,5,6,7,8,9]
# result = map(lambda x : x * 2, nums)
# print(list(result))
#A just 3 line short code.

#===>> use lambda function only when it is single expression fn or fn is used only once


#IF STATEMENTS
# is_male = True
# if is_male:
#     print("you are a male.")
# else:
#     print("you are a female.")

# OR OPERATOR ==> {if anyone is true then it's going to print the first one.}
# is_tall = True
# is_male = False
# if is_male or is_tall:
#     print("you are a male or tall or both.")
# else:
#     print("you are neither male nor tall.")

# AND OPERATOR ==> {if anyone is false then it's going to print the second one.}
# is_male = True
# is_tall = True
# if is_male and is_tall:
#     print("you are a tall male.")
# else:
#     print("you are either not male or tall or both.")

# elif (else if) operator
# is_male = True
# is_tall = True
# if is_male and is_tall:
#     print("you are a tall male.")
# elif is_male and not is_tall :
#     print("you are a short male.")
# elif not is_male and is_tall :
#     print("you are not a male but tall.")
# else:
#     print("you are neither not male nor tall.")

# if statements and comparison operators (>=,<=,==,>,<,!=)
# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3 :
#         return num1
#     elif num2 >= num1 and num2 >= num3 :
#         return num2
#     else:
#         return num3
# result = max_num(395,399,167)
# print(result)

#  BUILDING A BETTER CALCULATOR
# num1 = float(input("Enter first number: "))
# op = input("Enter operation: ")
# num2 = float(input("Enter second number: "))
# if op == "+":
#     print(num1 + num2)
# elif op =="-":
#     print(num1 - num2)
# elif op == "*":
#     print(num1 * num2)
# elif op =="/":
#     print(num1 / num2)
# else:
#     print("invalid operation")

# SET
# sets are not in order that's why we can't know the exact position of the elements in sets{=> no indexing}
# my_set = {1,2,2,3,5}
# print(my_set[2])

# sets do not allow the duplicates, if founds then they remove it by themselves.
# my_set = {1,2,2,3,5}
# print(my_set)

#tuples are immutable, thus they be fit in the lists and sets as objects
# my_lists = [("apple",3), (True,False), (1,2,3,4)]
# print(my_lists[1])
# print(my_lists[1][0])

# add an element
# my_set = {1,2}
# my_set.add(3)
# print(my_set)
#
# add multiple element
# my_set = {1,2}
# my_set.update([3,4],(5,6),{7,8})
# print(my_set)

#discard() and remove() ==> to remove a single element
#my_set = {1,2,3,4}
#my_set.discard(3)
#print(my_set)
#print(my_set.discard(5)) ==> doesn't shows error
# my_set.remove(3)
# print(my_set)
# print(my_set.remove(5)) ==> shows error

#union and intersection
# x = {1,2,3}
# y = {2,3,4}
# x.union(y)
# print(x)
# a = x.union(y)
# print(a)

# x = {1,2,3}
# y = {2,3,4}
# x.intersection(y)
# print(x)
# a = x.intersection(y)
# print(a)

#pop() ==> removing the first element mostly as a default
# x = {1,2,3,4,5,6,9}
# a = x.pop()
# #print(a)
# print(x)

#keeping common elements
# x = {1,2,3,4}
# y = {1,2,5,6}
# x.intersection_update(y)
# print(x)
# print(y)

# removing the common elements
# x = {1,2,3,4}
# y = {1,2,5,6}
# x.difference_update(y)
# print(x)
# print(y)

# printing those elements that are not in both sets
# x = {1,2,3,4}
# y = {1,2,5,6}
# x.symmetric_difference_update(y)
# print(x)
# print(y)

#FROZEN SETS ==>> are IMMUTABLE (unchangeable) and thus HASHABLE (value remains same throughout the program lifetime)
#thus we can use only immutable elements like str, int and tuples in the frozenset, not mutable like lists and sets.

# frozen_set = frozenset([(1,2),3,4,"abdul",5])
# print(frozen_set)

# not all operations of sets are applied here except union, intersection, difference and symmetric_difference
#we can't use update operations in frozenset, we should have to assign another variable or should print directly
# a = frozenset(["abdul","arif",19,20])
# b = frozenset(["sufiyan","hassan",18,19])
# x = a.intersection(b)
# print(x)

#DICTIONARY
#METHODS TO CREATE DICTIONARIES:
#1. using {}
# car = {
#     'brand' : 'ford',
#     'model' : 'Mustang',
#     'year' : 1964
# }
# print(car['model'])
# print(car.get('owner','henry ford'))

#2 using dict() constructor
#with a keyword argument
# d = dict(a = 1, b = 2, name = "Arif")
# print(d)

#with list / tuples pairs
# d = dict([('a',1), ('b',2), ('c',3)])
# d1 = dict((('d',4),('e',5),('f',6)))
# d2 = dict((['has',4],['have',10]))
# d3 = dict(({'f',9},{'j',99},{'s',87})) # not idiomatic in python

# with a zip of keys and value
# keys = {'a','b'}  # we can use any of the brackets [],{},() or no brackets at all.
# values = {1,2}
# d = dict(zip(keys,values))
# print(d)

#3 using dict.fromkeys() ==> every keys will have same single value that is provided
# d = dict.fromkeys(['a','b','c'],0)
# print(d)

# using unpacking(**)
# d1 = {'a':1}
# d2 = {'b':2}
# d3 = {'c':3}
# merged = {**d1, **d2, **d3}
# print(merged)

#another way
# d1 = {'x':1}
# merge = dict(**d1, y = 2 )
# print(merge)

#MODIFYING THE ELEMENTS
# car = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1964
# }
#
# car['year'] = 2002
# print(car['year'])
# car['color'] = 'red'
# print(car['color'])

# ATTRIBUTES AND OPERATIONS
# print(dir(dict)) # total 44 operations
# car = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1964
# }
# print(car.clear())
# vehicle = car.copy()
# print(vehicle)
# print(car.pop('year'))
# print(car)
# print(car.popitem())
# print(car)
# print(car.setdefault('brand'))
# print(car)
# print(car.setdefault('brand', 'kia'))
# print(car)
# bus = dict([('public','gov bus'), ('private','pvt bus')])
# bus1 = {
#     'brand': 'lamborghini',
#     'model': 'xyz',
#     'year': 1992
# }
# car.update(bus)
# print(car)
# car.update(bus1)
# print(car)

# update is used to merge two dictionaries or iterable key-value pairs
# d = {'a' : 1}
# d.update({'b':2,'c':3},d = 4)
# print(d)
# d.update([('e',5)])
# print(d)

# merge operator (|)
# a = {'x' : 1 , 'y' : 2}
# b = {'x' : 3 , 'z' : 4}
# c = a|b
# print(c)
# a |= b
# print(a)

#LOOPS
# WHILE LOOPS
# condition = 1  #starting point of the loop
# while condition <= 10:  #condtion over which the program loops
#    print(condition)  #instructions if the above condition is found true
#    condition += 1  # adding +1 consecutively till the condition becoming true.
#
# print("not meeting the requirements.")  #prints if the above condition becomes false

# command = ""
# while command != "exit":
#     command = input("Enter command: ")
#     print("you entered : ", command)

# user = ""
# while True :    # while True is an infinity loop controlled by [break]
#     user = input("type 'exit' to quit: ")
#     if user == 'exit' :
#         break
#     print("you typed: ", user)

# i = 0
# while i < 5:
#      i += 1
#      if i == 3 :
#          continue  # skips the rest of the loop if the condition meets
#      print(i)

# while True :
#     num = int(input("Enter a number(0 to stop):"))
#     if num < 0 :
#         print("Negative numbers are not allowed.")
#         continue     #==> skips the round
#     if  num == 0 :
#         print("Progress stopped")
#         break      #==> finish the entire loop
#     else:
#         print("You've entered: ", num)

#RANDOM MODULE
# import random
# a = random.randrange(1,10, 1)
# print(a)

# BUILDING A GUESS GAME

# secret_word = "eagle"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False                  #===> it is a boolean flag
# puzzle ="puzzle: flies above the sky"
# print(puzzle)
# while guess != secret_word and not out_of_guesses :   # here not out_of_guesses means 'true' True and True → True
#     if guess_count < guess_limit :
#        guess = input("Guess a word: ")
#        guess_count += 1
#     else:
#         out_of_guesses = True
# if out_of_guesses :
#    print("Out of guesses, YOU LOSE!")
# else :
#      print("You guessed the word, YOU WON"

#WITHOUT USING A BOOLEAN FLAG
# secret_word = "python"
# guess = ""
# guess_count = 1
# guess_limit = 3
#
# while guess != secret_word and guess_count <= guess_limit:
#     print(guess_count, " out of ", guess_limit, " left" )
#     guess = input("Enter guess: ")
#     guess_count += 1
#
# if guess == secret_word:
#     print("You guessed the word correctly, You win!")
# else:
#     print("Out of guesses, you lose!")

#FOR LOOP   #loop goes through each item's in the list one by one and  prints them whether they are string, lists or any numbers in range
# for letters in "python":
#     print(letters)

# for i in range(0,10,2): #if range(5),starts from zero and goes upto 5 but not include it.  ==> same as (start,stop,step)
#     print(i)

# friends = [ " abdul ", " sufiyan "," hassan " ]  # we can use any of them i.e. [],(),{} sets are unordered
# for index in friends:
#     print(index[3])     # we can also know each item one by one and get theirs particular index items too

#LOOPING WITH ELSE
# for i in range(3):
#     print(i)
# else:
#     print("loop is over.")

#using break statement
# for i in range(10):
#    if i == 4:
#        break    # immediately exits the program and not go further at this point
#    print(i)

#using continue statement
# for i in range(10):
#    if i == 4:
#        continue   # just skips the value
#    print(i)

#looping operations through dictionaries
# we can find keys and values in similar way mentioned below
# d = {'a':1, 'b':2}
# for keys in d.keys():   #better way to do that
#     print(keys)

# d = {'a':1, 'b':2}
# for keys in d:         #simple way to do the same thing
#     print(keys)

#for finding key-values pairs together we use .items()
# d = {'a':1, 'b':2}
# for keys,values in d.items():    #better way to do that
#     print(keys,values)
#
# d = {'a':1, 'b':2}
# for item in d.items():    #simple way to do the same thing
#     print(item)

# for i in frozenset([1,2,3]):
#     print(i)

#LOOPING WITH ENUMERATE
# colors = ['red', 'green', 'blue', 'yellow']
# for index , color in enumerate(colors):
#     print(index , color)

#LOOPING WITH ZIP
# cars = ['bmw', 'audi', 'toyota']
# colors = ['red', 'green', 'blue', 'yellow']
# for color , combination in zip(cars,colors):
#     print(color , combination)

# names = ['John', 'Michael', 'Jim', 'Jenny']
# scores = (100, 90, 80, 70)
# general_proficiency = {'b','c','d'}
# overall = frozenset([2,4])
# for result in zip(names, scores, general_proficiency , overall):
#     print(result)

#NESTED for LOOP
# for i in range(2):
#     for j in range(3):    #working process discussed in the notebook
#         for k in range(2):
#           print(i, j, k)

# LIST COMPREHENSIONS   {compact 'for' loops}
# squares = [x/2 for x in range(5)]
# print(squares)

#sum of all even numbers from 1 to 100
# total_numbers = 0
# for i in range(1,101):
#     if i % 2 == 0:
#        total_numbers += i
#        print(total_numbers)

# print(sum(num for num in range(2, 101, 2)))     #shorter version or method

# for i in range(1,10,2):
#     print(i, end = "")    # we can use any operator in between the strings, and it's gonna simply place the operator in between all values.

#BUILDING AN EXPONENTIAL FUNCTION

# def raise_to_power(base, exponent):
#     result = 1
#     for i in range(exponent):
#         result = result * base
#     return result
# print(raise_to_power(2, 3))

#2D LISTS
# numbers =[
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
# for row in numbers:
#     for col in numbers:
#       print(col)
# for row in A:
#    print(row[1])
# print(len(numbers))    # it gives the no. of rows
# print(len(numbers[0])  # it'll give the no. of columns of the matrix

# TRANSPOSING A MATRIX
# USING LOOP
# A = [[1,2,3],
#      [4,5,6],
#     ]
#   # we can also assign the dimensions for no. of rows and columns
    # rows = len(A)
    #cols = len(A[0])   # and further modifications or Amendment{making formal corrections or improvements.} required.

# transpose = [[0 for i in range(len(A))]for j in range(len(A[0]))]
#
# for i in range(len(A)):           #for row index
#    for j in range(len(A[0])):      #for column index
#         transpose[j][i] = A[i][j]  #swaps the value of A into transpose which is the actual literal meaning of transpose.
#
# print(transpose)

#USING LIST COMPREHENSIONS
# A = [[1,2,3],
#      [4,5,6],
#      ]
# transpose = [[A[i][j] for i in range(len(A))]  for j in range(len(A[0]))]
     #first part creates columns so we give it the range of row  (inner list comprehension)
     #second part creates row so we give ut range of column   (outer list comprehension)
# print(transpose)

#using numpy
# import numpy as np
# A = np.array([[1,2,3],
#      [4,5,6],
#      ])
# A_transpose = A.T
# print(A_transpose)

# A = [[1,2,3],
#      [4,5,6],
#      ]
# flat = [val for row in A for val in row]
# print(flat)

# matrix =[
#     [1, 9, 3],
#     [4, 5, 6],
#     [7, 8, 1],
#     [0]
# ]
# import copy
# copy_matrix = copy.deepcopy(matrix)
# print(copy_matrix)
# print(sum(copy_matrix[1]))

# max_val = max(max(row) for row in matrix)
# min_val = min(min(row) for row in matrix)
# print(max_val)
# print(min_val)

#SEARCHING FOR A VALUE IN A MATRIX
# matrix_A =[
#     [1, 9, 3],
#     [4, 5, 6],
#     [7, 8, 1],
#     [0]
# ]
# def find_value(matrix, target):
#     for i, row in enumerate(matrix):
#        for j, val in enumerate(row):
#
# print(find_value(matrix_A, 1))   #we can either directly put the matrix value here or just the variable that is assign to the matrix
#     #this will give the index of the target

#MODIFIED FUNCTIONS TO FIND ALL THE OCCURRENCE
# matrix_A =[
#     [1, 9, 3],
#     [4, 5, 6],
#     [7, 8, 1],
#     [8]
#     ]
# def find_value(matrix,target):
#     positions = []     #stores the (row,col) values
#
#     for i,row in enumerate(matrix):
#         for j,val in enumerate(row):
#             if val == target:
#                 positions.append([i,j])
#
#     return positions if positions else None
# print(find_value(matrix_A,8))   #now we can know each positions of the target present in the matrix.

# d = {
#     0: {0: 'a', 1: 'b'},
#     1: {0: 'c', 1: 'd'},
# }
# print(d)
#
# matrix_A =[
#     [0],
#     [4, 5, 6],
#     [7, 8, 1],
#     ]
# transpose = list(map(list, zip(*matrix_A)))
# print(transpose)


# copy = matrix_A[:]
# # [0] = 7
# matrix_A[2][1] = 5
# print(copy)
# # print(matrix_A)

# SYS MODULE
# import sys
# print(dir(sys))
# print(len(dir(sys)))
# print(sys.path)

# TO FILTER OUT ONLY FUNCTIONS
# import sys
# import types
# funcs = [name for name in dir(sys) if isinstance(getattr(sys,name),types.BuiltinFunctionType)]
# print(f"total functions : {len(funcs)}")
# print(funcs)

# BUILDING A TRANSLATOR  #==> basically building a translator that converts vowels of the phrase into letter 's'
# def translator(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.lower() in "aeiou" :    #makes every letter smaller and then cheks if it matches with aeiou or not
#             if letter.isupper():     #if letter is upper then
#                 translation = translation + "S"      #it's gonna append the 'S' in the translation variable(which is empty initially)
#             else:
#                 translation = translation +"s"   #same action with different parameters as told above
#         else:
#             translation = translation + letter  # if the letter isn't any vowel then it will append the original letter in the translation
#     return translation                #finally the translation string is returned to the caller
#
# print(translator(input("Enter a phrase: ")))

#TRY/EXCEPT

# try:
#    value = 10 / 2
#    num = int(input("enter a number: "))
#    print(num*num/num**2)
# except ZeroDivisionError as a:
#    print(a)
# except ValueError as err:
#     print(err)
#
# finally:
#     print("project done")

# reading files
# arif_biodata = open("arif.txt","r")
# for arif_lineage in arif_biodata:
#     print(arif_lineage.strip())   # prints each line cleanly
# arif_biodata.close()

# MODULES
# are basically a python file that contains a bunch of useful functions, variables, and classes etc.

#CREATING MY OWN MODULE NAMED "arif_module.py"
#we can't write the file here using file write("w") we've to do it manually.  ==> done
# Now we can import that file using import

# import arif_module
# print(arif_module.roll_dice(10))

# pip   ===> a program that is used to install any external modules
# import docx   ==> as we've already installed it using pip and then uninstall again

# CLASSES AND OBJECTS
# class Car:
#     def __init__(self, brand , model):
#         self.brand = brand
#         self.model = model
#
# car1 = Car("Toyota", "Mustang")
# print(car1.brand, car1.model)


# INHERITANCE

# from chef import Chef
#
# class Master_chef(Chef):
#
#     def make_special_dish(self):
#         print("The chef makes a nalla.")
#
#     def make_paya(self):
#        print("The chef makes paya.")
# my_chef = Master_chef()
# my_chef.make_special_dish()

#ENCAPSULATION

# class Car:
#     def __init__(self, brand , model):
#         self.__brand = brand
#         self.model = model
#
# car1 = Car("Toyota", "Mustang")
# print(car1.__brand, car1.model)

arr = [2,5,9,4]
arr[arr.index(5)] = 99 #if you dont 
print(arr)
