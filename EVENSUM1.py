# cook your dish here
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    T = int(data[0])
    idx = 1
    out = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = [int(x) for x in data[idx : idx+N]]
        idx += N
        total_sum = sum(A)
        has_even = any(x % 2 == 0 for x in A)
        has_odd = any(x % 2 != 0 for x in A)
        if total_sum % 2 == 0:
            if has_even:
                out.append("Yes")
            else:
                out.append("No")
        else:
            if has_odd:
                out.append("Yes")
            else:
                out.append("No")
    print('\n'.join(out))
if __name__ == '__main__':
    solve()
