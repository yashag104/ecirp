values = input().split()
N = int(values[0])
M = int(values[1])
sand = []
for _ in range(N):
    sand.append(0)
for _ in range(M):
    data = input().split()
    l = int(data[0])
    r = int(data[1])
    A = int(data[2])
    upgrade = r - l + 1
    each_upgrade = float(A / upgrade)
    for _ in range(upgrade):
        while not r == (l-1):
            sand[r-1] += each_upgrade
            r -= 1
print(" ".join(f"{amount:.4f}" for amount in sand))
