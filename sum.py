num=int(input("Enter number:"))
sum=0
while num>0:
    a=num%10
    sum=sum+a
    num=num//10
print("The sum is",sum)



num2=int(input("Enter number:"))
rev=0
while num2:
    d=num2%10
    rev=rev*10+d
    num2=num2//10
print("Reverse",rev)

