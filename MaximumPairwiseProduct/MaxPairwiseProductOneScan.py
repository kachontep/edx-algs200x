# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

i, j = 0, 1
for k in range(n):
    if a[i] < a[k]:
        i, j = k, i
print(a[i]*a[j])
