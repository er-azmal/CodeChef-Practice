# cook your dish here
n=int(input())
for i in range(n):
    x=int(input())
    l=list(map(int,input().split()))
    r=list(map(int,input().split()))
    score=0
    best_score=0
    best_rate=0
    index=0
    for j in range(x):
        score=l[j]*r[j]
        if score>best_score:
            best_score=score
            best_rate=r[j]
            index=j+1
        elif score==best_score:
            if r[j]>best_rate:
                best_rate=r[j]
                index=j+1
    print(index)
                
        
        