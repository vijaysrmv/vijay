# find out the area and circumference of circle using class
pi=3.14
class circle:
    def __init__(self,radius):
        self.r=radius
    def getarea(self,radius):

        area=pi*radius*radius
        return area
    def getcircumference(self,radius):

        circum=2*pi*radius
        return circum
b=5
a=circle(b)
print(a.r)
print(a.getarea(b))
print(a.getcircumference(b))
# make the information of student
dict={}
class student:
    def __init__(self,name,rollnumber):
        self.n=name
        self.r=rollnumber
    def display(self,name,rollnumber):
        print("name of the student is",name)
        dict["name"]=name
        print("Roll number of the tudent is ",rollnumber)
        dict["rollnumber"]=rollnumber
    def setage(self):
        a=input("enter the age of student")
        dict["age"]=a
        return "the age of the student is",a

    def setmarks(self):
        a=input("enter the marks of the student")
        dict["marks"]=a
        return "marks of the studet is",a
c="vijay"
d=6
b=student(c,d)
print(b.display(c,d))
print(b.setage())
print(b.setmarks())
print("you enterd the following data of student")
print(dict)
# convert temperature into degree celcius to farneheit
class temperature:
    def celcius(self,temp):
      temperature=(9/5)*temp-32
      return temperature
    def fahrenhit(self,temp):
        temperature=(5/9)*temp+32
        return temperature
a=temperature()
te=int(input("enter the temperature in farneheit"))
print("temperature in degree celcius is",a.celcius(te))
tem=float(input("enter the temperatre in degree celcius"))
print("teperature in farneheit",a.fahrenhit(tem))

# movie detail
dict={}
class moviedetail:
    def __init__(self,artistname,year,rating):
        self.a=artistname
        self.b=year
        self.c=rating
    def diplay(self,a,b,c):
        print("the artist name of movie is ",a)
        dict["artsitname"]=a
        print("year of release is",b)
        dict["year"]=b
        print("rating of movie is ",c)
        dict["rating"]=c

    def add(self):
        actressname=input("enter the actrees name ")
        dict["actressname"]=actressname
        moviename=input("enter the movie name")
        dict["movie"]=moviename
        return actressname,moviename
j=input("enter the artistname")
k=input("year of release")
l=input("enter the rating")
s=moviedetail(j,k,l)
s.diplay(j,k,l)
s.add()
print(dict)
 # make a class animal
class animal:
    def animal_attribute(self):
        print("All animal is mammal")


class tiger(animal):
    def tiger_attribute(self):
        print("tiger is king off all animal")


a = tiger()
print(a.animal_attribute())
print(a.tiger_attribute())

# check the code
class a:
    def f(self):
        return self.g()
    def g(self):
        return 'b'
class b(a):
    def g(self):
        return 'a'
x=a()
y=b()
print(y.f())
print(x.g())
print(y.g())
# output of the equation is
#a
#b
#a

# calculate the area of rectanle and square
class shape:
    def __init__(self,length,breath):
        self.length=length
        self.breath=breath
    def area(self):
        area=self.length*self.breath
        return area
class rectangele(shape):
      print("the area of the rectangle is")
class square(shape):
      print("the area of the square is")

a=int(input("enter the side "))
b=int(input("enter the another side"))
z=shape(a,b)
x=rectangele
y=square
if a==b:
    print("the area of the square is")
    print(y.area(z))

else:
    print("the area of the rectangle is")
    print(x.area(z))




