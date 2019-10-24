#Program to find if a given number is part of fabonacci and a factorial

num=int(input("enter any number "))

check1=0
check2=0
l=0
j=0
n=1
while(l<99):
    m=n
    n=n+j
    j=m
    if(num==n):
        check1=1
        break
    l+=1
if(check1==1):
    print("a fabonacci digit at place",l+3)
else:print("not a part of fabonacci")

n=2
sum=1
while(n<=num):
    sum=sum*n
    if(sum==num):
        check2=1
        break
    n+=1
if(check2==1):
    print("factorial of",n)
else:
    print("not a factorial")

    

