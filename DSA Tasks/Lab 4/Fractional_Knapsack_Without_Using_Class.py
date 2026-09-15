def fractional_knapsack(values, weights, capacity):

    items = list(zip(values, weights))

    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    current_weight = 0
    total_profit = 0.0

    for value, weight in items:
        if current_weight + weight <= capacity:

            current_weight += weight
            total_profit += value
        else:

            remain = capacity - current_weight
            total_profit += (value / weight) * remain
            break

    return total_profit

value = [60, 100, 200, 100]
weight = [10, 50, 50, 20]
capacity = 90

profit = fractional_knapsack(value, weight, capacity)
print("Profit:", profit)