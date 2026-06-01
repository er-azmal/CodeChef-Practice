t = int(input())
for i in range(0,t):
    x,y,a = map(int,input().split())
    # write your code here
    print("YES" if ((a>=x) and (y>a)) else "NO")