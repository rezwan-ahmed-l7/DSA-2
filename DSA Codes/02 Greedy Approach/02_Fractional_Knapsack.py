class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

items = [ Item(60, 10), Item(100, 50), Item(120, 30), Item(100, 20) ]

capacity = 50

# Sort by value per weight (highest first)
items.sort(key = lambda x: x.value / x.weight, reverse = True)

current_weight = 0
total_profit = 0.0

for item in items:
    if current_weight + item.weight <= capacity:
        # Take the whole item
        current_weight += item.weight
        total_profit += item.value

    else:
        # Take only the remaining capacity
        remaining = capacity - current_weight
        fraction = remaining / item.weight
        total_profit += item.value * fraction
        break

print(total_profit)