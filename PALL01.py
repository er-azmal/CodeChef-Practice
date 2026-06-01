# cook your dish here
n=int(input())
for i in range (n):
    x=int(input())
    t=x
    rev=0
    while(x>0):
        d=x%10
        rev=rev*10+d
        x//=10
    if (rev==t):
        print("wins")
    else:
        print("loses")