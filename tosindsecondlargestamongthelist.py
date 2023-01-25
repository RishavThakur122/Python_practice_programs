if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split(' ')))
    arr.sort()
    z=max(arr)
    while max(arr)==z:
        arr.remove(z)
    print(max(arr))    
