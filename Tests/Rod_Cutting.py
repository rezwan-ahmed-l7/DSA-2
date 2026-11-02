def rod_cutting(prices, n):
    solution = []
    for i in range(n + 1):
        row = [0] * (n + 1)
        solution.append(row)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            
            if i > j:
                solution[i][j] = solution[i - 1][j]
                
            else:
                solution[i][j] = max(
                    solution[i - 1][j], 
                    prices[i - 1] + solution[i][j - i]
                )

    return solution[n][n]

prices = [1, 5, 8, 9, 10, 17, 17, 20]
n = 8
print(rod_cutting(prices, n))