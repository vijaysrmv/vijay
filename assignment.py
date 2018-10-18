#create a list
list=['vijay','vinay','komal']
print(list)
#Concatinate a list
list=list+['vinod']
print(list)
# Count the list
print(list.count('vijay'))
print(len(list))
# sort the list
list1=['e','b','k','g']
list1.sort()
print("sorted list is",list1)
#sort the two list
list=list+list1
list.sort()
print(list)
# Counteven and odd number in a list

num_list4 = [1,2,3,4,5,6,7,8,9,10]

odd_nums=[]
even_nums=[]

for x in num_list4:
    if x % 2 == 0:
        even_nums.append(x)

    else:
        odd_nums.append(x)


print(even_nums)
print(odd_nums)
print(len(odd_nums))
print(len(even_nums))
#string to Uppercase
str="vijay"
print(str.upper())
#check the string is alphanumeric
str.isalpha()
print(str.isalnum())
#replace the string with my name
str1="my name is vinay"
str2=str1.replace("vinay","vijay sharma")
print(str2)

