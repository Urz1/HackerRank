from collections import defaultdict

n, m = map(int, input().split())

indices = defaultdict(list)
for i in range(1, n + 1):
    word = input()
    indices[word].append(i)
for _ in range(m):
    alpha = input()
    if alpha in indices:
        print(' '.join(map(str, indices[alpha])))
    else:
        print(-1)
