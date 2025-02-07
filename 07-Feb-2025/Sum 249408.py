# Problem: Sum - https://codeforces.com/contest/1742/problem/A

def sum_value(t, m, k):
    if t + m == k or t + k == m or m + k == t:
        print(True)
    else:
        print(False)
        
if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        t, m, k = map(int, input().split())
        sum_value(t, m, k)
