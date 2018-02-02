# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

for i in range(2):
    k = 0
    for j in range(1, n-i):
        if a[k] < a[j]:
            k = j
    a[n-1-i], a[k] = a[k], a[n-1-i]

print(a[n-1]*a[n-2])
