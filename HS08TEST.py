# cook your dish here
x,y=input().split()
x,y=int(x),float(y)
if((x%5==0) and (x+0.5)<=y):
    d=y-x
    print(d-0.5)
else:
    print(y)