t = int(input())
for i in range(0,t):
    x,y = map(int,input().split())
    # write your code here
    sum=x+y
    print("YES" if sum>6 else "NO")