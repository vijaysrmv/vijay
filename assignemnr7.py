# read a file
file=open("pr.py",'r')
print(file.read())
# count the frequenc of word in file
fname=input("enter the file name")
word=input("enter the word to be searched")
k=0
with open('fname','r') as f:
    for line in f:
        words=line.split()
        for i in words:
            if i==word:
                k=k+1
print("ocurence of the word")
print(k)
# copy the content of one file to another file
file=open("vijay.txt",'r')
dsta=file.read()
file.close()
file=open("first.txt",'w')
store=file.write(dsta)
print(store)
# copy the file and sort it

with open("first.txt",'r') as f:
    for i in f:
        words=i.split()

        print(words)
        words.sort()
        print(words)

