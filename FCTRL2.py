# cook your dish here
n=int(input())
for i in range(n):
    x=int(input())
    fact=1
    for j in range (1,x+1):
        fact*=j
        
    print(fact)