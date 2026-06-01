# cook your dish here
n=int(input())
x=list(map(int,input().split()))
e=0
o=0

for i in x:
    if i%2==0:
        e+=1
    else:
        o+=1
        
if e>o:
    print("READY FOR BATTLE")
else:
    print("NOT READY")