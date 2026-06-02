# cook your dish here
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    y=list(map(int,input().split()))
    if sum(y)<=b:
        print("Yes")
    else:
        print("No")