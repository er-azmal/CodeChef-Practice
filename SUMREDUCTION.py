# cook your dish here
import sys
def solve():
    data = sys.stdin.read().split()
    if not data: return
    T = int(data[0])
    idx = 1
    out = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = [int(x) for x in data[idx : idx+N]]
        idx += N
        total_sum = sum(A)
        or_sum = 0
        for x in A:
            or_sum |= x
        if total_sum == or_sum:
            out.append("Yes")
        else:
            out.append("No")
    print('\n'.join(out))
if __name__ == '__main__':
    solve()