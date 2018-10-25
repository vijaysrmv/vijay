
# calculate the area of sphere
pi=3.14
def area_sphere(r):
    area=4*pi*r*r
    return area
ans=area_sphere(5)
print("area is equal to",ans)

# printmultiplication table of n
n=int(input("enter the number"))
for i in range(1,11):
    print(n*i)

# calculate the power of number
def power(x,y):
    if y==1:
        return x
    else:
        return x*power(x,y-1)
x=3
y=4
print("result",power(x,y))

# check the number is perfect or not
list=[]
n=6
for i in range(1,10):
     x=n%i

     if x==0:

       print(i,end="")
       list.append(i)

print(list)
b=len(list)
c=0
for i in list[0:b-1]:
    j=c
    c=i+j

print(c)
d=1
for i in list[0:b-1]:
    j=d
    d=i*j

print(d)
if c==d:
    print("numer us perfect")
else:
    print("number is not oerfect")
