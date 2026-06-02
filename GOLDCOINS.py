# cook your dish here
n=list(map(int,input().split()))
d=n[2:4:1]
e=n[:2:1]
for i in range(len(d)):
    if d[i]>d[i+1]:
        print(e[i])
    elif d[i]<d[i+1]:
        print(e[i+1])
    break
    