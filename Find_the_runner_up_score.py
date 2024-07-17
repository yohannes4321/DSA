if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr1=list(arr)
    arr1.sort(reverse=True)
    m=arr1[0]
    a=[i for i in arr1 if (i <m)]
    print(a[0])
      
