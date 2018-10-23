# check the leap year
print("choose the option for which u want to check the leap year")
print("\n 1 Day in february month \n2 Day in Year \n 3 Year")
b=int(input("enter the number"))
if b==1:
    c=int(input("enter the total day in february month"))
    if c==29:
        print("leap year")
    else:
        print("This year does not belong to leap year")
elif b==2:
    c=int(input("enter the Total day in year"))
    if c==366:
        print("leap year")
    else:
        print("this year does not belong to leap year")
elif b==3:
    a=int(input("enter the year which you want to check"))
    if a/4:
        print("the given year is leap year")
    else:
        print("year is no leap")
else:
    print(" you choose WRONG option please retry the option")

# Check weather the given dimension are of square and rectangle
length=int(input("enter the length"))
breadth=int(input("enter the breadth"))
if(length==breadth):
    print("the given dimesion are of square")
else:
    print("the given dimension are of rectangle")

# Take the input age of 3 people and check the youngest and oldest


a=int(input("enter the age of first person"))
b=int(input("enter the age of second person"))
c=int(input("enter the age of third person"))
if a>b and a>c:
    print("First person is older than second and third person")
    if b>c:
        print("Third person is the younger among three person")
    else:
        print("Second person is the younger among three person")

elif b>a and b>c:
    print("Second person is older the first and third person")
    if a>c:
        print("Third  person is the younger among three person")
    else:
        print("First person is the younger among three person")
elif c>a and c>b:
    print("Third person is older than first and second person")
    if a>b:
        print("Second person is the younger among three person")
    else:
        print("First person is the younger among three person")
else:
    print("All three person have same age")

 # Ask user to enter age sex and marital status

a=int(input("enter the age"))
b=input("enter the sex male or female")
c=input("marital status")
if b=='f':
    print("  she will work only in urbn areas")
elif b=='m':
    if 20<a<=40:
        print("he may work in anywhere")
    elif 40<a<60:
        print("he will work in urban area only")
    else:
        print("error")
else:
    print("the given data is error")
# Discount of 10% given by owner to the customer if purchase quantity is more than 1000

a=int(input("enter the number of quantity of product"))
if a>=11:
    b=(a*100)-(a*100)/10
    print("the cost of product is:",b)
else:
    b=a*100
    print("the cost of product is:",b)

# Take 10 integer from user and print on screen

c=[]
for i in range(0,10):
    b=int(input("enter the number"))
    c.append(b)
print("you enterd the following number")
print(c)



# make a list input by user and other list store the square of first list
z=[]
d=[]
for i in range(0,4):
    b=int(input("enter the number"))
    z.append(b)
print("you enterd the following number")
print(z)
for i in z:
    x=pow(i,2)
    d.append(x)
print(d)

# make a list and seperate them by data types

lst=[1,1.2,'vijay']
a=[]
b=[]
c=[]
for i in lst:
    z=type(i)
    if z==int:
        a.append(i)
    elif z==float:
        b.append(i)
    else:
        c.append(i)
print(a)
print(b)
print(c)

# make a star triangle

for i in range(1,5):
    if i==1:
        print('*')
    elif i==2:
        print('**')
    elif i==3:
        print('***')
    else:
        print('****')
# Also this program can be written as
for i in range(1,5):
    print('*'*i)

# Take input from user to make a list. again make a another list and search in first list
    # question nahi aa raha h
    # send me the solution of this
    
# write an infinity loop condition is never true
    while True:
       print("infinity loop")