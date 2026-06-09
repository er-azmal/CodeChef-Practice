# cook your dish here
import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    N = int(input_data[0])
    print((N // 20) + 1)
if __name__ == '__main__':
    solve()