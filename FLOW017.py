# cook your dish here
n=int(input())
for i in range(n):
    x,y,z=map(int,input().split())
    d=[x,y,z]
    d.sort()
    print(d[1])