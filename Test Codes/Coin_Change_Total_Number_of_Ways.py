def count_ways(coins, amount):
    n = len(coins)

    solution = []
    for i in range(n + 1):
        row = [0] * (amount + 1)
        solution.append(row)

    for i in range(n + 1):
        solution[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, amount + 1):

            if coins[i - 1] > j:
                solution[i][j] = solution[i - 1][j]

            else:
                solution[i][j] = solution[i - 1][j] + solution[i][j - coins[i - 1]]

    return solution[n][amount]


coins = [1, 2, 5]
amount = 11
print(count_ways(coins, amount))
