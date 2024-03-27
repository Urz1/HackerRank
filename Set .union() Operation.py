# Enter your code here. Read input from STDIN. Print output to STDOUT
English = int(input())
studentE = set(map(int,input().split()))
French = int(input())
studentF = set(map(int,input().split()))
print(len(studentF|studentE))
