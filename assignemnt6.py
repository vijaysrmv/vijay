# check theprogram
a=3
try:
    if a<=4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError:
    print("Divide by zero is not possible")
# check the program
l=[1,2,3]
try:
    print(l[3])
except IndexError:
    print("List is out of range")
# program to depict raising exception
try:
    raise NameError("hi there")
except NameError:
    print("an exception")
    raise
# function handling
def AbyB(a,b):
    try:
        c=(a+b)/(a-b)
    except ZeroDivisionError:
        print("a/b resultin zero")
    else:
        print(c)
AbyB(20,10)
AbyB(2,2)
# error
import re
try:

 p=re.compile('ab*',re.IGNORECASE)
 print(p.match('ABcdab'))
except ImportError:
    print("the import error take place")
try:
    l=[1,2,3]
    print(l[3])

except IndexError:
    print("list out of range")
try:
    a=int(input("enter the number"))
    print(a)
except ValueError:
    print("integer is pure number")

