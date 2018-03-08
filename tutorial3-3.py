# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 17:36:01 2018

@author: WEI
"""

class MyClass:
    variable = " blash"
    def function(self):
        print("This is a message inside the class")
        

myobjectx = MyClass()
myobjecty = MyClass()

# accessing object variable 

myobjecty.variable = "yackity"
print(myobjectx.variable)
print(myobjecty.variable)

# accessing object Functions

myobjectx.function()

# Excercise

class Vehicle:
    def __init__(self,name, kind, color, value):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." %(self.name,
                                                  self.color,
                                                  self.kind, self.value)
        return desc_str
    
car1 = Vehicle("Feb","SUV","red",100000)

# Dictionary

phonebook = {'John': 93877564, "Jack": 88384843, "Jill":37474745}
for name, number in phonebook.items():
    print("Phone name of %s is %d" %(name, number))
    
del phonebook["John"]
phonebook.pop("Jill")
print(phonebook)

if "Jake" not in phonebook:
    print("Jake is not listed in the phonebook")
if "Jake" in phonebook:
    print("Jake is listed in the phonebook")
    
# module

import draw
def play_game():
    ...
def main():
    result = play_game()
    draw.draw_game()
# this means that if this script is excuted, then 
# main() will be excuted
if __name__ =="__main__":
    main()

#############################################################
    
##           A proactical introduction to Python programming
    
#############################################################
    
# 1.3

temp = eval(input('Enter a temperature in Celsius: '))
print('In Fahrenheit, that is ', 9*5*temp + 32)
 
num1 = eval(input('Enter the first number: '))
num2 = eval(input('Enter the second number: '))
print('The average of the numbers you entered is', (num1 + num2)/2)   

# 1.4 Typing thins in 

print('Hello world!')
print ('Helo world!')
print(  'Hello world!'  )
    
# 1.5 getting input 
name = input("Enter your name: ")
print('Hello, ', name)

num = eval(input("Enter a number: "))
print('Your number squared: ' , num * num)

# 1.6 printing 

print('Hi there')
print('3 + 4')
print(3+4)
print('The value of 3 + 4 is', 3+ 4) # automatically insert spaces
print('A',1,'XYZX',2)

print('The value of 3 + 4 is', 3 + 4,'.')
print('The value of 3+ 4 is', 3 + 4, '.', sep = '')

print('on the first line')
print('on the second line')

print('on the first line', end = '')
print('on the second line')

# 1.8 variable

temp = eval(input("Enter a temperature in Celsius: "))
f_temp = 9/5*temp + 32
print("In Fahrenheit, that is", f_temp)
if f_temp > 212:
    print("That emperature is above the boiling point")
if f_temp < 32:
    print("That temperature is below the freezing point")
    
# exercise
    
print('****************')
print('****************')
print('****************')

print('****************')
print('*              *')
print('****************')

print('*')
print('**')
print('***')
print('****')

print((512-282)/ (47.48 + 5))

num = eval(input("Enter a number: "))
print('The square of 5 is ',num*num,'.', sep = '')

x = eval(input("Enter a number: "))
print(x, 2*x, 3*x, 4*x, 5*x, sep = '---')

weight = eval(input("Enter the weight in Kg: "))
print("In pounds, that is", 2.2*weight)



## For loops
for i in range(10):
    print('Hello')
    
for i in range(3):
    num = eval(input('Enter a number: '))
    print ('The square of your numbr is', num*num)
print('The loop is now donw')

print('A')
print('B')
for i in range(5):
    print('C')
    print('D')
print('E')

# The loop variable

for i in range(3):
    print(i + 1, '--Hello')
    
for i in range(100):
    print(i)
    
for wacky_name in range(100):
    print(wacky_name)
    

for i in range(5,0,-1):
    print(i, end =' ')
print('Blast off!')

# 2.4 A trickier example
for i in range(6):
    print('*'*6)
for i in range(4):
    print('*'*(i+1))

# Numbers 

# 3.1 Integers and Decimals Numbers
from random import randint
x = randint(1,10)
print('A random bumber between 1 and 10: ', x)

from math import sin, pi
print("Pi is roughly", pi)
print('sin(0)= ', sin(0))

print(abs(-4.3))
print(round(3.336, 2))
print(round(345.2,-1))

# 3.6 get in help in python

import math
dir(math)

help(math.floor)

# Using the shell as a Calculartor


# If statements
# 4.1 

from random import randint
num = randint(1,10)
guess = eval(input('Enter your guess: '))
if guess == num:
    print("You got it!")
else: 
    print('Sorry. The number is ', num)


# 4.2
# >, >= ==, != and or not
if grade>=80 and grade<90:
    print("Your grade is a B.")
if score >1000 or time < 20:
    print('Game over.')
if not(score >1000 or time > 20):
    print('Gmae continuue')
    
# 4.4 elif
grade = eval(input("Enter your score: "))
if grade >= 90:
    print('A')
if grade>=80 and grade<90:
    print('B')
if grade>=70 and grade<80: print("C")
if grade>60 and grade<70: print("D")
if grade<60: print("F")



grade = eval(input("Enter your score: "))
if grade>90:
    print('A')
    
elif grade >= 80:
    print('B')
elif grade >=70:
    print('C')
elif grade>=60:
    print('D')
else: print('E')


# exercise

temp = eval(input("Enter the temperature: "))
unit = input("What unit? Celsius or  Fahrenheit, enter C or F: ")
if unit == 'C':
    print("In Fahrenheit, that is", 9/5*temp+32)
elif unit == 'F':
    print("In celsius, that is", 5/9*(temp-32))
else:
    print("You can enter either C or F")
    

from random import randint
for i in range(10):
    a = randint(1,10)
    b = randint(1,10)
    s = eval(input( str(a)+  '*'+ str( b) + "=: "))
    if s == a*b :
        print("Right.")
    else: 
        print("Wrong.  ","The answer is", a*b)
    

now = eval(input("Enter hour: "))
m = eval(input("am (1) or pm (2)? "))
ahead = eval(input("How many hours ahead? "))
if m == 2:
    if (now + 12 + ahead) // 12 %2 == 0:
        print((now + 12 + ahead )% 12, "am")
    else: print((now + 12 + ahead) % 12, "pm")
else: 
    if (now + ahead) // 12 %2 == 0:
        print((now + 12 + ahead) % 12, "am")
    else: print((now + 12 + ahead) % 12, "pm")
    

# 5.1 counting
# 5.2 summing
# 5.3 swapping 
x = 3
y = 4
x,y = y,x
print("X=",x , " Y =", y)
# Falg variable
# Maxes and mins
# comments
# simple debugging
# Example programming

# 
count = 0
for i in range(1,101):
    if i**i % 10 == 1:
        count += 1
print(count)

from math import log
n = eval(input("Enter a integer: "))
sum = -log(n)
for i in range(n):
    sum += 1/(i+1)
print(sum)
    

n = eval(input("Enter a integer: "))
sum = 0
for i in range(n):
    if n%(i+1) == 0:
        sum = sum + (i+1)
print(sum)

x = 3
y = 4
z = 5
x,y,z = y,z,x


## String

#6.1 Basics
s = 'Hello'
t = "Hello"
m = """ This is a long string that is spread
across two lines"""

num = eval(input("Entera number"))
string = input('Enter a string: ')
len('Hello')
'Ab' + 'cd'
'Hi'*4

# 6.3 The in operator
if t in 'aeiou': print("Yes")
# in, not in 

# 6.4 Indexing
# slicing
s = 'abcdefghij'
s[2:5]
s[:5]
s[-2:]
s[:]
s[1:7:2]
# 6.6 Changing individual characteristics or a string
# 6.7 Looping
for c in s:
    print(c)
    
# 6.8 String method
s = "wei peng"
s.lower()
s.upper()
s.replace('w','f')
s.count('e')
s.index('e')
s[0].isalpha()

# Escape characters
filename = 'c:\\programs\\file.py'



## List
# 7.1 basic
L = [1,2,3]
nums = [1,2,3,4,5,6,
        3,4,5,6,9,
        2,1,2,]
L = eval(input("Enter a list: "))
print('The first element is  ', L[0])

L =[1,2,3]
print(L)
L = [1,2.718, 'abc', [5,6,7]]

# 7.2 Similarities to strings

# len in not in, +, *, 
# build in functions
# len sum , min, max, 

# 7.4 List method
L = [1,4,9,16,25]
L.append(36)
L.sort()
L.count(25)
L.index(16)
L.reverse()
L.remove(36)
L.pop(1)
L.insert(2,3.1415)

M = L[:]

from random import randint
L = []
for i in range(50):
    L.append(randint(1,100))
    L = L + [randint(1,100)]

# 8 More with lists 
from random import choice
from random import sample
names = ['Joe','Bob','Sue','Sally']
current_player = choice(names)
team = sample(names, 2)

from random import shuffle
shuffle(names)
print(names)

# split

s = 'Hi! This is a test.'
print(s.split())

from string import punctuation
for c in punctuation:
    s = s.replace(c,"")
print(s)

from string import punctuation
s = input('Enter a string: ')
for c in punctuation:
    s = s.replace(c,'')
s = s.lower()
L = s.split()

word = input("Enter a world: ")
print(word, 'appears', L.count(word), 'times.')

s = '1-800-271-8281'
print(s.split('-'))

# 8.3 join


from random import shuffle
word = input("Enter a word: ")

letter_list = list(word)
shuffle(letter_list)
anagram = ''.join(letter_list)
print(anagram)

# 8.4 List comprehensions

string  = 'Hello'
L = [1,14,5,9,12]
M = ['one','two','three','four','five','six']

[0 for i in range(10)]
[i**2 for i in range(1,8)]
[i*10 for i in L]
[c*2 for c in string]
[m[0] for m in M]
[i for i in L if i< 10]
[m[0] for m in M if len(m)==3]


L = [[i,j] for i in range(2) for j in range(2)]

# Using list comprehensions

L = [randint(1,100) for i in range(50)]
L = [i**2 for i in L]

L = [[1,2],[3,4],[5,6]]
M = [[y,x] for x,y in L]
print(M)

# Two-dimensional lists
L = [[1,2,3],
     [4,5,6],
     [7,8,9]]

from pprint import pprint
pprint(L)

import numpy as np
count = np.sum([1 for r in range(3) for c in range(3) if L[r][c]% 2 == 0])
count
L = [[0]*50 for i in range(100)]
# picking out rows and columns
c = 2
L = [[1,2,3],
     [4,5,6],
     [7,8,9]]
print([L[i][c] for i in range(len(L))])

# Flattening a list
[j for M in L for j in M]

# exerc
# 1
s = input("Enter a string: ")
from string import punctuation
for c in punctuation:
    s.replace(c,"")
L = s.split()
L.count('a') + L.count('an')+ L.count('the')
# 2

s = input("Enter 5 integers, seperated by space: ")
L = s.split()
s = "+".join(L)

# 3
s = input('Enter a sentece: ')
print(s[2])
print(s[::3])

# 4
s = input("Enter a sentence: ")
from random import shuffle
L = s.split()
shuffle(L)
s = " ".join(L)


s = input("Enter a sentence: ")
from random import shuffle
from string import punctuation
for c in punctuation:
    s = s.replace(c,"")
L = s.split()
print(L)
L[0] = L[0].lower()
shuffle(L)
L[0]  = L[0].replace(L[0][0], L[0][0].upper())
s = " ".join(L) + "."
print(s)

# 5
quote_of_day = ["My heart is always in my work","You are the apple of my eye.","One apple a day, keeps the doctor away"]
from random import choice
print(choice(quote_of_day))

# 6
from random import sample
sample(range(48),6)

# 7
# 8
#9
# 10
# censoring words program (hard problem)


s = input("Enter som text: ")
curse = ['darn','dang','freakin','heck','shoot','sex',,'cheating']

punc = []
id = []
L = []
for c in s:
    L.append(c)
for i in range(len(L)):
    if L[i] in punctuation:
        punc.append(L[i])
        id.append(i)
        count += 1
    
from string import punctuation
for c in punctuation:
    s  = s.replace(c,'')
        
L = s.split()
for i in range( len(L)):
    if L[i] in curse:
        L[i] = '*' * len(L[i])

LL = []
ss = " ".join(L)
for c in ss:
    LL.append(c)
print(LL)
for i in range(len(punc)):
   LL.insert(id[i],punc[i])
# test if a telephone number
s = input("Enter a phone number: ")
L = [0,1,2,4,5,6,8,9,10,11]
CL = [3,7]
LL = [0,2,3,4,6,7,8,10,11,12,13]
CLL = [1,5,9]
if len(s) == 12:
    id = sum(1 for i in CL if not s[i]=="-") +sum(1 for i in L if not s[i].isdigit())
    if id >0 : print("Invalid")
    else: print("Valid")

    
elif len(s) ==14:
    id = sum(1 for i in CL if not s[i]=="-") +sum(1 for i in L if not s[i].isdigit())
    if id > 0: print("Invalid")
    else: print("Valid")
else:
    print("Invalid")
    
# 
L = ["You", "are", "the", "apple" ,"of","my","eye"]
[s[1:] for s in L ]
[len(s) for s in L]
[s for s in L if len(s)>=3]

#14
count = 0
for i in range(100,1000):
    s = []
    while( i > 0.01):
        s.append(i%10)
        i = i //10
    ss = s[:]
    s.reverse()
    if  ss == s:
        print(ss)
        count += 1
print(count)

#
L = [[1]+ [0]*i for i in range(10)]
[j for M in L for j in M]

#
L = [2,3,5,7,11,12,17,19,23,31,37,41,43,47]
gap = [L[i]-L[i-1] for i in range(1,len(L))]
print(max(gap))
sum([1 for i in gap if i ==2])/(len(gap))

#
L = [[1,2,3,4],[4,5,6,7],[8,9,10,11,12],[13,14,15,16]]
sum([sum(M) for M in L])

from random import randint
L = [[randint(1,100) for j in range(10)]for i in range(10) ]
from pprint import pprint
pprint(L)
    
print(max(L[2]))
print(min([ L[i][6] for i in range(len(L))]))

#
[[(i+j+1) % 2 for j in range(8)] for i in range(8)]

# check if magic square
L = [[1,8,12,13],[14,11,7,2],[15,10,6,3],[4,5,9,16]]
sumL = [sum(L[i]) for i in range(len(L))] + [sum([L[i][j] for i in range(len(L))]) for j in range(len(L))]+ [sum([L[i][i] for i in range(len(L))]) ] + [sum([L[len(L)-1-i][i] for i in range(len(L))])]

indicator = sum([1 for i in range(1,len(sumL)) if sumL[i] != sumL[0]])
if indicator > 0: print('no')
else: print("Magic square")

# Memory game 


from random import choice
import string
from string import punctuation
L = []
count = 0
while(count < 18):
    c = choice(punctuation)
    if c not in L:
        L.append(c)
        L.append(c)
        count  += 1
print(L)


from random import shuffle
shuffle(L)
LL = [[L[6*i+j] for j in range(6)] for i in range(6)]
from pprint import pprint
pprint(LL)

# 
L = [1265,12171,23257,34548,45970,56236,67324,78084,89872,99414]
LL = []
for l in L:
    s = []
    while( l > 0.01):
        s.append(l % 10)
        l = l // 10
    s.reverse()
    LL.append(s)
LL[0].insert(0,0)
print(LL)

for i in range(10000,100000):
    s = []
    while( i > 0.99):
        s.append( i % 10)
        i = i // 10
    s.reverse()
    
    ind =  [1 for i in range(len(LL))  if sum([1 for j in range(5) if LL[i][j] == s[j]]) ==1]
    if sum(ind) == 10: 
       print(s)
       
# 26 
       
       
 # WHILE
temp = 0
while(temp!=-1000):
    temp = eval(input("Enter a temperature (-1000 to quit): "))   
    if temp != -1000:
        print("In Fahrenhert, that is", 9/5*temp)
    else: 
        print("Bye!")
    
from random import randint
secret_num = randint(1,10)
guess = 0
while(guess != secret_num):
    guess = eval(input("Guess the secret number: "))
print('You finally got it')        
        
    
for i in range(10):
    print(i)
    
i = 0 
while(i < 10 ):
    print(i)
    i = i + 1
    
    
# 9.1
# 9.2 
# break statement
for i in range(10):
    num = eval(input("Enter a number: ")) 
    if num < 0:
        break
i = 0
num = 1
while i < 10 and num > 0:
    num = eval(input("Enter a number: "))
    i = i + 1


temp = 0 
while temp != -1000:
    temp = eval(input("Enter a temperature:"))
    if temp != -1000:
        print(9/5*temp+ 32)
    else:
        print("Bye")

while True:
    temp = eval(input("Enter a temperature:" ))
    if temp == -1000:
        print("Bye!")
        break
    else: 
        print(9/5*temp + 32)
    
# 9.4 The else statement
    
i = 2
num = 19
while i < num and num %i != 0:
    i = i + 1
if i == num:
    print("Prime")
else: 
    print("Not a prime")

for i in range(2,num):
    if num % i == 0:
        print("Not a prime")
        break
else: print("Prime")


# 9.5

from random import randint
secret_num = randint(1,100)
num_guess = 0
guess = 0
while(guess != secret_num and num_guess <=4):
    guess = eval(input("Guess a number: "))
    num_guess += 1
    if guess == secret_num:
        print("You got it!")
    elif guess > secret_num:
        print("LOWER",5- num_guess, "guess left.\n")
    else:
        print("HIGHER", 5 - num_guess, "guess left,\n")
if (num_guess ==5 and guess != num_guess):
    print("You lose. The correct number is ", secret_num)

from random import randint
secret_num = randint(1,100)
for num_guess in range(5):
    guess = eval(input("guess a number: "))
    num_guess += 1
    if guess >  secret_num: 
        print("LOWER",5- num_guess, "guess left.\n")
    elif guess < secret_num:
        print("HIGHER", 5 - num_guess, "guess left,\n")
    else: 
        print("You got it")
        break
else: 
    print("You lose. The correct number is ", secret_num)
    
    
#
for i in range(1,51):
    print(i)
i =1
while(i < 51):
    print(i)
    i = i + 1
# 2
s = "AmericanEnglish"
while s!="":
    print(s[0])
    s = s[1:]
s = "AmericanEnglish"
while(len(s)>0):
    print(s[0])
    s = s[2:]
    
    
# 3
while True:
    weight = eval(input("Enter the weight in kilogrmas (-1 to quit): ") )
    if weight < 0:
        print("The weight is invalid, please enter again: ")
    else:
        print("The weight in pounds, that is ", weight * 1.1)
        break

# password
num_try = 5
s = "ML17@Omega"

for i in range(num_try):
    password = input("please enter your password:")
    if password != s:
        print("Invalid!")
    else:
        print("You are logged in th esystem.")
        break
else:
    print("You are kicked off!")

# 5
s = []
count_A = 0
while True:
    score = eval(input("Enter a score: "))
    if score > 0:
        s.append(score)
        if score > 90:
            count_A += 1
    else:
        break
print(count_A)
print(sum(s) /len(s))

#  7

s = "AmericanEnglish"
c = input("Enter a letter: ")
i = 0 
while(i < len(s)):
    if s[i] == c:
        print(i)
        break
    i = i + 1
else:
    print("No such letter in the string")
    
    
# 
s = "AmericanEnglish"
c = input("Enter a letter: ")
found = False
i = 0
while(i < len(s) and not found):
    if s[i] == c:
        found = True
        print(i)
    i = i + 1
if i == len(s) and found == False:
    print("No such a letter in the String")

    
    
# 
s = "AmericanEnglish"
c = input("Enter a letter: ")
for i in range(len(s)):
    if s[i] == c:
        print(i)
        break
else:
    print("No such letter in the string.")
    
# 8
    
a = eval(input("Enter a number: "))
b = eval(input("Enter another number: "))
a,b = max(a,b), min(a,b)

while( b != 0):
     a, b = b, a % b
print(a)
     
# 9
a = eval(input("Enter a number: "))
import numpy as np
e = 1
count = 0
while(e > 1e-10):
    b,a = a,(a + 5/a)/2 
    count += 1
    e = abs(a-b)
    
print(e,count)
    
# 10
L = ['you', 'are','the','apple','of','my','eye']
for i in range(len(L)):
    s = []
    j = 0
    while(j < len(L[i])):
        if L[i][j] not in s:
            s.append(L[i][j])
        j = j + 1
    if len(s) == len(L[i]):
        print(L[i])
        
# 11

L = [[0]*5 for i in range(5)]
f = [j for M in L for j in M]
seq = [i for i in range(len(f))]
seq

from random import choice
s= []
i = 0
while(i < 5):
    id = choice(seq)
    s.append(id)
    del seq[id]
    i = i + 1
for i in s:
    f[i] = 1
L = [[f[5*i+j] for j in range(5)] for i in range(5)]
print(L)


# 12

L = [randint(0,1) for i in range(7)]
print(L)
i = 0
while(i < len(L)):
    if L[i] == 0:
        L[i] = 1
        print(L)
        break
    i = i + 1
else:
    print("No zeros.")

# 13
# Rock-Paper-Scissor
s = ['R','P','S']
dict = {'R':0,'P':1,'S':2}
L =[[0,0,1],[1,0,0],[0,1,0]]
LL =[[0,1,0],[0,0,1],[1,0,0]]

count_player = 0
count_computer = 0

while(count_player < 3 and count_computer < 3):
    player = input("Enter your choice (R,P,S):")
    computer = random.choice(s)
    print("Computer's choice: ", computer)
    count_player += L[dict[player]][dict[computer]]
    count_computer +=  LL[dict[player]][dict[computer]]

if (count_player > count_computer):
    print("You Win! ")
else:
    print("You lose!")
    
 # 14
 
money = 100
from random import randint
while(money > 0 and money <200):
    money += (-10 + 19 * randint(0,1))
print(money)
 
 
# 15
L = ['Canada','America','Britich','China','Japan']
from random import randint
country = choice(L)
country = [c for c in country]
print(country)

s = ['-' for i in range(len(country))]
for guess in range(5):
    c = input("Enter a letter:")
    guess += 1
    id = [i for i in range(len(country)) if country[i] == c]
    print(id)
    for i in id:
        s[i] = c
    print("".join(s))
    if s == country: 
        print("You got it!")
        break
else:
    print("no more tries!")
    
    
    
# 16 MEMORY GAME

from random import choice
import string
from string import ascii_uppercase
L = []
count = 0
while(count < 18):
    c = choice(punctuation)
    if c not in L:
        L.append(c)
        L.append(c)
        count  += 1
print(L)


from random import shuffle
shuffle(L)
LL = [[L[6*i+j] for j in range(6)] for i in range(6)]
from pprint import pprint
pprint(LL)  
    

# str int float int list
list(range(5))
list('abc')

for i in range(1,1000):
    s = str(i)
    if s == s[::-1]:
        print(i)

birthday = 'January 1, 1991'
year = int(birthday[-4:])
print("You are", 2017 - year, "years old!")

import numpy as np

answer = np.sum([int(c) for c in str(num)])

num = 47.2
ipart = int(num)
dpart = num - int(num)

# Boolean
x = (6==6)
a=b=c = 0
a,y,z = L
x,y,z = 1,2,3
# if a==b==c==c==0:
# if 1<a<b<5:
# 
L = ['Joe','Bob','Sue','Jimmy','Todd',\
     'Mike','John','Amy','Edger','Sam']

# 10.6 pass
# 10.7 String formatting
a = 23.60 * 0.25
print('The tip is {:.2f}'.format(a))

bill = 23.60
tip = 23.60 * .25
print('Tip: ${:.2f}, Total: ${:.2f}'.format(tip, bill + tip))

print('{:3d}'.format(2))
print('{:3d}'.format(25))
print('{:3d}'.format(138))


print('{:^5d}'.format(2))
print('{:^5d}'.format(122))
print('{:^5d}'.format(12824))

print('{:<5d}'.format(2))
print('{:<5d}'.format(122))
print('{:<5d}'.format(12824))


print('{:,d}'.format(100000000))

print('{:8.2f}'.format(89.3423))
print('{:^8.2f}'.format(89.3423))
print('{:<8.2f}'.format(89.3423))

print('{:10s}'.format('Hello'))
print('{:^10s}'.format('Hello'))
print('{:<10s}'.format('Hello'))

# 10.8 nested loop
# exercise:

list(range(3,100,3))
# 2

print('{:.1f}'.format(123.45))

# 3
s = input("Enter a word: " )
L = list(s)
done = False
p = 1
LL = L[:]
for i in range(len(L)-1):
    for j in range(i+1, len(L)):
        if L[i]> L[j]:
            L[j],L[i] = L[i], L[j]
print("".join(L))

# 4 
print('{:6.2f}'.format(120.035))
    

# 5
suits = ['Hearts','Diamonds','Clubs','Spades']
values =['One','Two','Tree','Four','Five','Six','Seven',
         'Eight','Nine','Ten','Jack','Queen','King','Ace']

# 6

L1 =['a','p','p','l','e']
L2 = ['p','e','a','r']
exist = False
i =j =0
while(i < len(L1) and exist == False):
    if L1[i] in L2:
        exist = True
        print(L1[i], "is in common.")
    i = i + 1
if i == len(L1): 
    print("Nothing in common")

# 7
L = [[1]*i for i in range(1,101)]
[i for M in L for i in M]


#8 
[i for i in range(10000) if i % 7 == 6]
# 
np.sum([1 for i in range(100) if '3' in str(i)])

# 10

#15 How many zeros of  100! 
import math
num = str(math.factorial(1000))
len(num)
np.sum([1 for c in num  if int(c) == 0])

# 17
done = False
score = []
while not done:
    s = input("Enter wining score-losing score: ")
    if s == 'done':
        done = True
    else: 
        win = int(s[:s.index('-')])
        loss = int(s[s.index('-')+1:])
        score.append(win)
        score.append(loss)
print(max(score))
print(min(score))

# 19
# 23 
L = [4,3,5,7,2,0,7]
LL = [[(i-1)%10,i, (i+1)%10] for i in L]

for a in LL[0]:
    for b in LL[1]:
        for c in LL[2]:
            for d in LL[3]:
                for e in LL[4]:
                    for f in LL[5]:
                        for g in LL[6]:
                            if a*10 + b + c*10 + d == e*100 + f* 10 +g:
                                print( a,b ,'+ ',c,d,' =' ,e,\
                                     f,g)
# 25
L = [[0,'M',0,'M',0],
     [0,0,'M',0,0],
     [0,0,0,0,0],
     ['M','M',0,0,0],
     [0,0,0,'M',0]]
LL = [[0]*7 for i in range(7)]
for i in range(len(L)):
    for j in range(len(L[i])):
        LL[i+1][j+1] = L[i][j]
from pprint import pprint

for i in range(len(L)):
    for j in range(len(L[i])):
        if L[i][j] == 0:
            L[i][j] = np.sum([1 for d_i in range(-1,2) for d_j in range(-1,2) if LL[i+1+d_i][j+1+d_j] == 'M'])
pprint(L)


# 30  Pascal triangle

num_row = eval(input("Enter the row: "))

LL =[]
L = [0] * (num_row)  +[1] + [0]*(num_row)
for j in range(num_row):
    LL.append(L)
    L = [0] + [L[i-1]+ L[i+1] for i in range(1,len(L)-1)] + [0]

for i in range(len(LL)):
    for j in range(len(LL[i])):
        if LL[i][j] != 0:
            print(LL[i][j], end =" ")
        else: 
            print("", end =" ")
    print()

# 32 Monte Carlo simulation

from random import randint
L = [ [randint(1,6) for i in range(6)] for i in range(10000)]
print(np.sum([1 for i in range(10000) if L[i][0]==L[i][1]==L[i][2]==L[i][3]==L[i][4]==L[i][5]]))

count = 0 
for M in L:
    if M[0]+4== M[1]+3 == M[2]+2 == M[3]+1 == M[4] or \
    M[1]+4 == M[2]+3 == M[3]+2==M[4]+1==M[5]:
        count += 1
        print(M)
print(count)
    
L = [randint(0,1) for i in range(200)]
count = 1 
maximum = 1
i = 1 
while i < len(L):
    if L[i]==L[i-1]:
        count += 1
    else: 
        maximum = max(maximum, count)
        count = 1
        
    i = i + 1
print(maximum)
    
#\
count = []

for i in range(1000):
    r = []
    time = 0
    while np.sum(r) < 5:
        r.append(randint(0,1))
        time += 1
    count.append(time)
print(np.sum(count)/ len(count))

# Dictionary
# 11.1 
d = {'A':100,'B':200}
d['A'] = 400
d['C'] = 500
del d['A']

# 11.2

deck = [{'value':i,'suit':c} for c in ['spades','clubs','hearts','dimaonds'] for i in range(2,15)]
from random import shuffle
shuffle(deck)

# 11.3
d = {'A':100, 'B':200}
d2 = d.copy()

letter = input("Enter a letter: ")
if letter in d:
    print("The value is", d[letter])
else:
    print('Not in dictionary')

for key in d:
    print(key)
for key in d:
    print(d[key])
list(d)
list(d.values())
list(d.items())
L = [x[0] for x in list(d.items()) if x[1]== 100]

d = dict([('A',100),('B',300)])
words = ['You','are','the','apple','of','my','eye']
d= { s: len(s) for s  in words}

# Counting words

text = open('romeoandjuliet.txt').read()

from string import punctuation
text = text.lower()
for p in punctuation:
    text = text.replace(p,'')
words = text.split()

d = {}
for w in words:
    if w in d:
        d[w] += 1
    else:
        d[w] = 1
print(d)

items = list(d.items())
items.sort()
for i in items:
    print(i)
    
items = list(d.items())
items = [(i[1],i[0]) for i in items]
items.sort()
for i in items:
    print(i)

# 1
done = False
dict_p  ={}
while not done:
    
    product = input("Enter the product (enter done to quit):")
    if product != 'done':
        price  = eval(input("Enter the price: "))
        dict_p[product] = price
    else:
        done = True
enough = False
while not enough:
    product = input("Enter the product that you want price( enter enough to quit): ")
    if product in dict_p:
        print(dict_p[product])
    elif product == 'enough':
        enough = True
    else:
        print(product, "is not in the dictionary.")

    
# 2
amount = eval(input("Enter a dollar amount: "))
for key in dict_p:
    if dict_p[key] <= amount:
        print(key, dict_p[key])

# 3
year = {'January':31,'Feburary':28,'March':31,'April':30,'May':31,'June':30,
        'July':31,'August':31,'September':30,'October':30,'November':30,'December':31}

month = input("Enter a month: ")
print(year[month])

L = list(year)
print(L.sort())

print([x[0] for x in year.items() if x[1] == 31])
items = year.items()

items = [(i[1],i[0]) for i in items]
items.sort()
print(items)

# 
login = {'wep15':'miss@lhh', 'weiprng':'ML17@Omega'}
username = input("Enter your user name: ")
if username in login:
    count = 0
    while(count < 5):
        password = input("Enter your password: ")
        count += 1
        if password == login[username]:
            print("you are logged in the system.")
            break
        else: 
            print("invald password")
    else: 
        print("You are run out of all tries.")
else:
    print("Invalid username")
    
# 5 

from string import punctuation
team = {}
done = False
while not done:
    s = input('Enter game scores: ')
    if s != 'done':
        for p in punctuation:
            s = s.replace(p,"")
        l = s.split()
        print(l)
        if l[0] in team:
            team[l[0]]['wins'] += int(l[1])
            team[l[0]]['losses'] += int(l[3])
        else:
            team[l[0]] = {}
            team[l[0]]['wins'] = int(l[1])
            team[l[0]]['losses'] = int(l[3])
        if l[2] in team:

            team[l[2]]['wins'] += int(l[3])
            team[l[2]]['losses'] += int(l[1])
        else:
            team[l[2]] = {}
            team[l[2]]['wins'] = int(l[3])
            team[l[2]]['losses'] = int(l[1])
    else:
        done = True

[team[x]['wins'] for x in team]
[x for x in team if team[x]['wins']>0]
# 6
deck
from random import shuffle
from random import choice
shuffle(deck)
player1 = random.sample(deck, 3)
deck = [x for x in deck if x not in player1]
player2 = random.sample(deck,3)

p1 = [x['value'] for x in player1]
p2 = [x['value'] for x in player2]
p1.sort()
p1.reverse()
print(p1)
p2.sort()
p2.reverse()
print(p2)
if  p1>p2:
    print("Player1, Win")
elif p2 > p1:
    print("Player2, Win")
else:
    print("draw")

# 9
shuffle(deck)
player = random.sample(deck,3)

player[0]['suit'] == player[1]['suit'] == player[2]['suit']
player[0]['value'] == player[1]['value'] == player[2]['value']
player = [(x['value'],x['suit']) for x in player]
player.sort()
player[0][0]+ 2== player[1][0]+ 1\
== player[2][0] and player[0][0]>=2

# 10

# 12

### Chapter 12 Text files
lines = [line.strip() for line in open('romeoandjuliet.txt')]
lines

s = open('romeoandjuliet.txt').read()
s= open('c:/Users/WEI/s650/ML-python/romeoandjuliet.txt'). read()

# 12.2 write to file
f = open('eritefile.txt','w')
print('This is line 1.', file = f)
print('This is line 2.', file = f)
f.close()
# over written

# 12.3 
lines = [line.strip() for line in open('score.txt')]
games = [line.split(',') for line in lines]

# 12.4 Wordplay
wordlist = [line.strip() for line in open('wordlist.txt')]
for word in wordlist:
    if len(word)== 3:
        print(word)
print([word for word in wordlist if len(word)==3])
print([word for word in wordlist if word[:2]=='gn' or word[:2]=='kn'])
print(np.sum([1 for word in wordlist if word[0] in 'aeiou']))

f = open('class_score.txt','w')
print('GWashington 83', file = f)
print('Pittsburgh 95', file = f)
print('NewYork 92', file = f)
f.close()

lines = [line.strip() for line in open('class_score.txt')]
print(lines)
lines =[line.split() for line in lines]
lines
[[x[0], int(x[1])+5] for x in lines]

# 2
# 3
f = open('logfile.txt','w')
print( 'Wei Peng, 14:22, 14:37', file = f)
print('Wanying Fu, 12:20, 13:40', file = f)
print('Omega, 1:00, 8:00', file = f)
f.close()
lines = [line.strip() for line in open('logfile.txt')]
lines = [x.split(',') for x in lines]
pprint(lines)

# 5
f = open('students.txt','w')
print('wei peng\twep15@pitt.edu\t555-3134', file = f)
print('wanying fu\twaf10@pitt.edu\t944-6588', file = f)
f.close()
lines = [line.strip() for line in open('students.txt')]
lines = [x.split('\t') for x in lines]
pprint(lines)

f = open('students2.txt','w')
for line in lines:
    s = line[0].split()
    s[0] = s[0][0].upper() + s[0][1:]
    s[1]= s[1][0].upper() + s[1][1:]
    line[2] = '412-'+ line[2]
    line[0]= " ".join(s)
    print(line, file = f)
f.close()


# Function 13
 
# return: end early
# local variables

def func1():
    for i in range(10):
        print(i)
def func2():
    i = 100
    func1()
    print(i)
    
func2()

def func1(x):
    x = x +1
def func2(L):
    L =  L + [1]
    print("excuted!")
def func3(L):
    copy = L[:]
    copy = copy + [1]
    
a = 3
M =[1,2,3]
func1(a)
func2(M)
print(a)
print(M)


# exercise
#1 
def rectangle(m,n):
    for i in range(m):
        print('*'* n)
rectangle(2,3)

# 
def add_excitement(L):
    L = L.append('!')
def add_excitement2(L):
    copy = L[:]
    copy = copy.append('!')
    print(copy)
L =['You','are','the','apple','of','my','eye']
add_excitement2(L)
L

# 3
def sumDigits(num):
    s = list(str(num))
    return np.sum([int(x) for x in s])

n = 65
print(sumDigits(n))

# 4
def digitRoot(num):
    s = list(str(num))
    while(len(s)>1):
        s = list(str(np.sum([int(x) for x in s])))
    return s

n = 29
print(digitRoot(n))

# 
def firstDiff(s1, s2):
    ss1 = s1 + '*'* max(0, len(s2)-len(s1))
    ss2 = s2  + '*' * max(0,len(s1)-len(s2))
    idex = 0
    while(idex < len(ss1)):
        if ss1[idex] != ss2[idex]:
            location = idex
            break
        idex += 1
    else:
        location = '-1'
    return location

firstDiff('watermelon','watermelon')


# 6 

# Ojected programming

class Example:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    
e = Example(8,6)
print(e.add())


# in python all variables are public 
from string import punctuation
class Analyzer:
    def __init__(self, s):
        for c in punctuation:
            s= s.replace(c,"")
        s = s.lower()
        self.word = s.split()
    def num_of_words(self):
        return len(self.word)
    def starts_with(self, s):
        return len([w for w in self.word if w[:len(s)]== s])
    def number_with_length(self, n):
        return len([w for w in self.words if len(w) == n])
s = 'This is a test of the class'
analyzer = Analyzer(s)
print(analyzer.num_of_words())
print('NUmber of words:', analyzer.starts_with('t'))
print(analyzer.word)

class Parent:
    def __init__(self,a):
        self.a = a
    def method1(self):
        print(self.a*2)
    def method2(self):
        print(self.a + ':!!')
class Child(Parent):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def method1(self):
        print(self.a*7)
    def method3(self):
        print(self.a + self.b)
p = Parent('hi')
c = Child('hi','bye')
print('Parent method1:', p.method1())
print('Parent method1:',p.method2())
print()
print('Child method1:',c.method1())
print('Child method2:',c.method2())
print('Child method3:',c.method3())



class Child(Parent):
    def __init__(self, a, b):
        Parent.__init__(self,a)
        self.b = b
    def print_var(self):
        Parent.print_var(self)
        print(self.b)

# 14.4 A playing-card example
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        names =['Jack','Queen','King','Ace']
        if self.value < 10 :
            return'{} of {}'.format(self.value, self.suit)
        else:
            return '{} of {}'.format(names[self.value-11], self.suit)

import random

class Card_group:
    def __init__(self, cards=[]):
        self.cards = cards
    
    def nextCard(self):
        return self.cards.pop(0)
    
    def hasCard(self):
        return len(self.cards) > 0
    
    def size(self):
        return len(self.cards)
    
    def shuffle_card(self):
        random.shuffle(self.cards)

class Standard_deck(Card_group):
    def __init__(self):
        self.cards = []
        for s in ['Hearts','Diamond','Clubs','Spades']:
            for v in range(2,15):
                self.cards.append(Card(v,s))
        

class Pinochle_deck(Card_group):
    def __init__(self):
        self.cards = []
        for s in ['Hearts','Diamond','Clubs','Spades']*2:
            for v in range(9,15):
                self.cards.append(Card(v,s))
        
        
deck = Standard_deck()
deck.shuffle_card()
new_card = deck.nextCard()
print("\n",new_card)
choice = input("Higher (h) or lower (l): ")
streak = 0

while(choice == 'h' or choice=='l'):
    if not deck.hasCard():
        deck = Standard_deck()
        
        deck.shuffle_card()
    old_card = new_card
    new_card = deck.nextCard()
    if (choice.lower()=='h' and new_card.value > old_card.value or\
        choice.lower() =='l' and new_card.value < old_card.value):
        streak += 1
        print('right! that is',streak,'in a row')
    elif (choice.lower()=='h' and new_card.value < old_card.value or\
          choice.lower() =='l' and new_card.value > old_card.value):
            streak = 0
            print("Wrong")
    else:
        print('Push')
    print('\n',new_card)
    choice = input('higher (h) or lower (l): ')


## Tic-Tac-Toy
class tic_tac_toe:
    def __init__(self):
        self.B=[[0,0,0],
                [0,0,0],
                [0,0,0]]
        self.player  = 1
        
    def get_open_spots(self):
        return [[r,c] for r in range(3) for c in range(3) if self.B[r][c] == 0]
    
    def is_valid_move(self, r,c):
        if 0<=r<=2 and 0<=c<=2 and self.B[r][c] == 0:
            return True
        else:
            return False
        
    def make_move(self, r, c):
        if self.is_valid_move(r,c):
            self.B[r][c] = self.player
            self.player = (self.player +2)%2 + 1
            
    def check_for_winner(self):
        for c in range(3):
            if self.B[0][c] == self.B[1][c] == self.B[2][c] !=0:
                return self.B[0][c]
        for r in range(3):
            if self.B[r][0] == self.B[r][1] == self.B[r][2]!=0:
                return self.B[r][0]
        if self.B[0][0] == self.B[1][1] == self.B[2][2] !=0:
            return self.B[0][0]
        if self.B[0][2]==self.B[1][1] == self.B[2][0] != 0 :
            return self.B[0][2]
        if self.get_open_spots() == []:
            return 0
        return -1

def print_board(game):
    chars = ['-','X','O']
    for r in range(3):
        for c in range(3):
            print(chars[game.B[r][c]], end=" ")
        print()
        
game = tic_tac_toe()

while game.check_for_winner() == -1:
    print_board(game)
    r,c = eval(input('Enter spot, player'+ str(game.player)+": "))
    game.make_move(r,c)
    
game.check_for_winner()
print_board(game)

# ex:

from tkinter import *
root = Tk()
mainloop()


from tkinter import *
def calculate():
    temp = int(entry.get())
    temp = 9/5*temp +32
    output_label.configure(text = " Converted: {:.1f}".format(temp))
    entry.delete(0,END)
    
root = Tk()
message_label = Label(text="Enter a temperature", font =('Verdana', 16))
output_label = Label(font = ("Verdana", 16))
entry = Entry(font = ('Verdana',16))
calc_button = Button(text="ok",font=("Verdana", 16), command = calculate)

message_label.grid(row = 0, column = 0)
entry.grid(row = 0, column = 1)
calc_button.grid(row = 0, column = 2)
output_label.grid(row =1, column = 0, columnspan = 3)

mainloop()
    
 
    
# Label

hello_label = Label(text='hello', font=('Verdana',16,'bold'),
                  bg = 'blue', fg = 'white')
hello_label.grid(row = 0, column = 0)
# Changing label property
label.configure(text = 'Bye')

label.configure(bg = 'white',fg = 'black')

label.configure(text ='a ={}, b = {}'.format(a,b))

# grid
    
lable1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column0, columnspan=2)
label4.grid(row=1,column=2)
label5.grid(row=2, column=2)
    
    
# Entry


entry = Entry()
entry.grid(row=0, column=0)

#
string_value = entry.get()
num_value = eval(entry.get())

entry.delete(0,END)
entry.insert(0,'hell0')


# Button
ok_button = Button(text ='ok')

from tkinter import *
def callback():
    label.configure(text ='Button clicked')
root = Tk()
label = Label(text="Not clicked")
button = Button(text='click me', command= callback)

label.grid(row=0, column=0)
button.grid(row=1, column=0)
mainloop()


from tkinter import *
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def callback(x):
    label.configure(text='Button {} clicked'.format(alphabet[x]))

root = Tk()
label = Label()
label.grid(row=1,column=0, columnspan=26)
button = [0]*26
for i in range(26):
    button[i] = Button(text =alphabet[i], command = lamcallback(x))
    button[i].grid(row=0,column=i)
mainloop()


# # tic-tac-toe

from tkinter import *
def callback(r,c):
    global player
    global stop_game
    if player == 'X' and states[r][c] == 0 and stop_game==False:
        b[r][c].configure(text='X')
        states[r][c] = 'X'
        player = 'O'
    if player == 'O' and states[r][c] == 0 and stop_game==False:
        b[r][c].configure(text='O')
        states[r][c] = 'O'
        player = 'X'
    check_for_winner()

def check_for_winner():
    global stop_game
    for i in range(3):
        if states[i][0]==states[i][1]==states[i][2]!=0:
            b[i][0].configure(bg='grey')
            b[i][1].configure(bg = 'grey')
            b[i][2].configure(bg = 'grey')
            stop_game = True
    for i in range(3):
        if states[0][i]==states[1][i]==states[2][i]!=0:
            b[0][i].configure(bg='grey')
            b[0][i].configure(bg = 'grey')
            b[0][i].configure(bg = 'grey')
            stop_game = True
    for i in range(3):
        if states[0][2]==states[1][1]==states[2][0]!=0:
            b[0][2].configure(bg='grey')
            b[1][1].configure(bg='grey')
            b[2][0].configure(bg='grey')
            stop_game = True
    for i in range(3):
        if states[0][0]==states[1][1]==states[2][2]!=0:
            b[0][0].configure(bg='grey')
            b[1][1].configure(bg='grey')
            b[2][2].configure(bg='grey')
            stop_game = True
    return stop_game
        
b = [[0]*3 for i in range(3)]
states =[[0]*3 for i in range(3)]
player = 'X'
stop_game = False

root = Tk()
for i in range(3):
    for j in range(3): 
        b[i][j] = Button(font=('Verdana',56),width=3, bg='yellow',
         command = lambda r=i,c=j: callback(r,c))
        b[i][j].grid(row=i,column=j)
    
mainloop()


# 16.2

from tkinter import *
root = Tk()

b = [0]*26
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(26):
    b[i] = Button(text = alphabet[i])
    b[i].grid(row = 0, column = i)
ok_button = Button(text = 'OK', font=('Verdana',24))
ok_button.grid(row = 1, column=0, columnspan=26)
mainloop()


# frame
from tkinter import *
root = Tk()
button_frame = Frame()
b = [0]*26
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(26):
    b[i] = Button(button_frame,text = alphabet[i])
    b[i].grid(row = 0, column = i)
button_frame.grid(row=0, column = 0)

julie = PhotoImage(file='giphy.gif')
ok_button = Button(image=julie , font=('Verdana',12))
ok_button.grid(row = 1, column=0)


mainloop()

label = Label(text='H1', bg = '#A202FF')
              
# 16.3 Image
julie = PhotoImage(file='juli.jpg')
label = Label(image = julie)
button = Button(image = julie, command=julie_callback())
label.configure(image=julie)



# Cnavas
from tkinter import *
root = Tk()

canvas = Canvas(width=2000, height=2000,bg='white')
canvas.grid(row=0,column=0)

canvas.create_rectangle(20,100,30,150, fill='red')
canvas.create_oval(20,100,70,180, fill='blue')
canvas.create_line(20,100,70,180, fill='green')

def create_circle(x,y,r):
    canvas.create_oval(x-r,y-r, x+r,y+r)

jolie = PhotoImage(file='giphy.gif')
canvas.create_image(100,100,image=jolie)

rect = canvas.create_rectangle(0,0,20,20)
canvas.itemconfigure(rect, fill='yellow')
canvas.coords(rect, 40,40,60,60)
mainloop()




canvas.delete(ALL)




































































    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

            







































        

















    
    


















        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        






















    
    
    
    
    
    
    
    
    















    






























































































































    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    















        
    
    






















        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        












































































        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    















































    














































    
    


















































































   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
























































    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


















            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

        















    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




















    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    































































































    




























































































































































































    



































































































































    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



