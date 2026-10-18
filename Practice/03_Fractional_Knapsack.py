values = [60, 100, 120, 100]
weights = [10, 50, 30, 20]
capacity = 50

items = list(zip(values, weights))
items.sort(key=lambda x: x[0] / x[1], reverse=True)

current_weight = 0
total_profit = 0.0

for value, weight in items:
    if current_weight + weight <= capacity:
        current_weight += weight
        total_profit += value
    else:
        remaining = capacity - current_weight
        fraction = remaining / weight
        total_profit += value * fraction
        break

print(total_profit)