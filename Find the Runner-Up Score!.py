if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    A = set(arr)
    A.remove(max(A))
    print(max(A))

    
