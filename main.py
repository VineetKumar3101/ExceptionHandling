print("----------------------------------------------")

#tryblock
import sys

a=input("Enter = ")
b=input("Enter = ")
res=0
try:
    res=a/b
except:
    print(sys.exc_info()[0],"ERror Occured")
    print("Do no divide by zeros")
print("Result = ",res)


print("----------------------------------------------")

res1=0
try:
    c=int(input("Enter = "))
    d=int(input("Enter = "))
    res1=c/d
except (ZeroDivisionError):
    print(sys.exc_info()[0],"ERror Occured")
except (ValueError):
    print("Input Integer")
print("Result = ",res1)

print("----------------------------------------------")