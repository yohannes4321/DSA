# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

def love(s):
    count = 0
    for i in range(len(st)):
        if s[i] != st[i]:
            count += 1 
    print(count)


if __name__ == "__main__":
    t = int(input())
    arr = []
    st = "codeforces"
    for i in range(t):
        s = input()
        love(s)