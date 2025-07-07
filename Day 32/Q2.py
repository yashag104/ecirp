def is_beautiful(n, a):
    count = 0
    i = 0
    while i < n:
        j = i
        while j < n and a[j] == a[i]:
            j += 1
        if (i == 0 or a[i - 1] > a[i]) and (j == n or a[j] > a[j - 1]):
            count += 1
        i = j
    return count == 1
t = int(input().strip())
results = []
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    if is_beautiful(n, a):
        results.append("YES")
    else:
        results.append("NO")
for result in results:
    print(result)
