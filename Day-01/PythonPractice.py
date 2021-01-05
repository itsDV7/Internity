#Print Name and Institute Name
print("Divyansh Chaudhary")
print("ASET")

#Multiply 2 numbers
print(2*3)

#Salary of 2 People
sal1=input("Salary1: ")
sal2=input("Salary2: ")
print(sal1)
print(sal2)

#Sum of list
list = [1,2,3]
print(sum(list))

#Largest of List
list = [1,2,3,4,6,5]
print(max(list))

#Smallest of List
list = [1,2,3,4,6,5]
print(min(list))

#Multiplies all items in list
list = [1,2,3]
print(list*3)
new_list = [i * 2 for i in list]
print(new_list)

#Create Tuple
t1=1,2,3
t2=(1,2,3)

#Tuples with different data types
t1 = 1,1.1,'apple'
print(t1)
print(type(t1))

#Tuples with numbers and print one item
t1 = (1,2,3)
print(t1[1])

#Add an item to tuple
t1 = 1,2,3
t2 = 4,5,6
t1 = t1+t2
t1 = t1+(7,)
t1 = t1[:3]+(777,)+t1[3:]
print(t1)

#Tuple to string
def tostring(tup):
    tup = ''.join(tup)
    return tup
t1 = 'a','b','c'
strg = tostring(t1)
print(strg)
print(type(strg))

#Create a Set
s1={1,2,3}
print(s1)
print(type(s1))

#Add member in a set
s1={1,2,3}
s1.add(4)
print(s1)

#Remove item from set
s1={1,2,3,4}
s1.remove(3)
print(s1)

#Remove if an item is present in set
s1 = {1,2,3,4,5}
item = int(input("Remove: "))
if item in s1:
    print("Removed: ",item)
    s1.remove(item)
else:
    print("Item not in set.")
print(s1)

#Remove if an item is present in dictionary
dct = {"name":"divyansh","sec":6,"enroll":8373,"age":20}
item = input("Remove: ")
if item in dct:
    dct.pop(item)
else:
    print("Not in dct")
print(dct)

#Add key to dictionary
dct = {"name":"divyansh","sec":6,"enroll":8373,"age":20}
dct["new"] = "entry"
print(dct)

#Concatinate dictionaries
dct = {}
dct1 = {"name":"divyansh","sec":6}
dct2 = {"enroll":8373,"age":20}
dct.update(dct1)
dct.update(dct2)
print(dct)

#Check if a key exists
dct = {"name":"divyansh","sec":6,"enroll":8373,"age":20}
item = input("Key: ")
if item in dct:
    print("Exists")
else:
    print("Not in dct")
print(dct)

#Program to convert one currency to another for 1000 records
import random
from forex_python.converter import CurrencyRates
Curr = CurrencyRates()
for i in range(1,11):
    rand = random.randint(1,5000)
    print(f"Currency{i} in $$: ",rand)
    rand = rand * Curr.get_rate('USD','INR')
    print(f"Currency{i} in (INR) Rs.: ", rand)

#Function that returns unique elements of a list
def unique(list):
    list_new = []
    for i in list:
        print(i)
        if i not in list_new:
            list_new.append(i)
    return list_new
l1=[5,1,2,3,4,4,5]
print(unique(l1))

#Simple Calculator
def add(n1,n2):
    return n1+n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    if n2 == 0:
        return print("Division by Zero not Possible!")
    return n1/n2
def sub(n1,n2):
    return n1-n2
def calc(ch,num1,num2):
    cases = {1:add(num1,num2),2:sub(num1,num2),3:mul(num1,num2),4:div(num1,num2)}
    print(cases[ch])
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n")
choice = int(input("Enter Choice: "))
if choice not in (1,2,3,4):
    print("Invalid Input")
else:
    numbr1 = int(input("Enter Number 1: "))
    numbr2 = int(input("Enter Number 2: "))
    calc(choice,numbr1,numbr2)

#Rock-Paper-Scissors game
from random import randint
def play(ch):
    if randint(1,3)==ch:
        print("Draw!")
    elif ch==1 & randint(1,3)==2:
        print("Computer Wins!")
    elif ch==2 & randint(1,3)==3:
        print("Computer Wins!")
    elif ch==3 & randint(1,3)==1:
        print("Computer Wins!")
    else:
        print("You Win")
print("Rock-Paper-Scissors Game!\n")
print("Your Choice:\n1. Rock\n2. Paper\n3. Scissors\n")
choice = int(input("> "))
if choice in (1,2,3):
    play(choice)
else:
    print("Enter value between 1 and 3\n")

