# cook your dish here
x=list(map(int,input().split()))
count=0
for i in x:
    if i>=10:
        count+=1
print(count)