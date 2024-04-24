if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list_t=list(arr)
    score=list(set(list_t))
    score.sort()
    print(score[-2])
