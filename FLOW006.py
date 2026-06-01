# cook your dish here
n=int(input())

for i in range(0,n):
    x=int(input())
    sum=0
    while(x>0):
        y=x%10
        sum+=y
        x=x//10
    print(sum)
    