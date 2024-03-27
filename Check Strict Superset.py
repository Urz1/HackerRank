# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int,input().split()))
n = int(input())
checker = True
for _ in range(n):
    sub = set(map(int,input().split()))
    if not A.issuperset(sub) or A == sub:
        checker = False
        break
    
print(checker)
        
    
    
