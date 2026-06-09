# cook your dish here
n=int(input())
for _ in range(n):
    N,B=map(int,input().split())
    tab=0
    tabe=0
    found=False
    for _ in range(N):
        W,H,P= map(int,input().split())
        tab=W*H
        if B>=P and tab>tabe:
            tabe=tab
            found=True
    if found:
        print(tabe)
    else:
        print("no tablet")
        
        