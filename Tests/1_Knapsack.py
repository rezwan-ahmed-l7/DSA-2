def knapsack(weights, values, capacity):
    n = len(weights)

    solution = []
    for i in range(n + 1):
        row = [0] * (capacity + 1)
        solution.append(row)

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):

            if weights[i - 1] > j:
                solution[i][j] = solution[i - 1][j]

            else:
                solution[i][j] = max(
                    solution[i - 1][j],
                    values[i - 1] + solution[i - 1][j - weights[i - 1]],
                )

    return solution[n][capacity]


weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7
print(knapsack(weights, values, capacity))
