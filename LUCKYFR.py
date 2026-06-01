# cook your dish here
n=int(input())
for i in range(n):
    x=int(input())
    d=str(x)
    count=0
    for j in d:
        if j == '4':
            count+=1
    print(count)
           