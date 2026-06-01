# cook your dish here
n=int(input())

for i in range(n):
    x,y=map(float,input().split())
    total=x*y
    if (x>=1000):
        d=(x*y)*0.1
        total=total-d
    print(total)
