from sys import stdin


def input(): return stdin.readline()


testcases = int(input())
results = []
for _ in range(testcases):
    values = input().split()
    customers = int(values[0])
    balance = int(values[1])
    withdrawals = list(map(int, input().split()))
    withdrawals.sort()
    customers_served = 0
    money_given = 0
    for withdraw in withdrawals:
        if customers == 0:
            break
        if money_given == balance:
            break
        money_given += withdraw
        customers_served += 1


    if customers_served == 0 or balance < 0 or int(values[1]) < 0:
        customers_served = -1
    results.append(customers_served)
for result in results:
    print(result)
