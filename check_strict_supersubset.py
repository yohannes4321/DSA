value = set(map(int, input().split()))
n = int(input())
other_sets=[set(map(int,input().split(" "))) for _ in range(n)]
def i_can_make_it(value,other_sets):
    for i in other_sets:
        if not(value >i):
            return False
    return True
print(i_can_make_it(value,other_sets))
