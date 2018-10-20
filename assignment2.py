
# split and store the value after typecasting (I didn't understand the question properlly)

dummy="vijay sharma ,dummy"

print(dummy.split('a'))
store=dummy.split('a')


# To check th pallindrome
str="malayalam"
c=str.lower()
a=tuple(c)
b=a[::-1]
if a==b:
    print(str, "is ","pallindrome")
else:
    print("not pallindrome")




# reverse the list
list=[1,2,3,4,5]
list.reverse()
print(list)


# Extract the uppercase from string
s="VijAy"
print("the given string is",s)
print("The uppercase letter in given string is")
for x in s:
    if x.isupper():
        print(x)















