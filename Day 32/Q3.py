MOD = 1000000007

N = int(input())
if N == 1:
    ways = 1
elif N == 2:
    ways = 2
elif N == 3:
    ways = 4

a, b, c = 1, 2, 4

for _ in range(4, N + 1):
    ways = (a + b + c) % MOD
    a, b, c = b, c, ways
print(ways)
