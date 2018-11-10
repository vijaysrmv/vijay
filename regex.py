# valid email id
import re
email=input("enter an input string")
m=re.match(r'[^@]+@[^@]+\.[^@]+',email)
if m:
    print("valid email")
else:
    print("false")
# valid mobile number
import re
s="917710393928"
match=re.match(r'(91/0)?[7-9][0-9]{9}',s)

if match:
    print("valid number")
else:
    print("not valid")








