N = int(input())

X = list(map(int, input().split()))

X.sort(reverse=True)

count = 0

for _ in X:
    first = X[0]
    if len(X) >= first:
        del(X[:first])
        count += 1
    else:
        pass

try:
    if X[0] == 1:
        count += 1
except:
    pass

print(count)
