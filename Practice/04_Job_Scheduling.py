profits = [25, 15, 30, 20, 12, 35, 5]
deadlines = [4, 3, 4, 2, 1, 3, 2]

jobs = list(zip(profits, deadlines, range(1, len(profits) + 1)))
jobs.sort(key=lambda x: x[0], reverse=True)

max_deadline = max(deadlines)
slot = [None] * (max_deadline + 1)

total_profit = 0

for profit, deadline, job_id in jobs:
    for t in range(min(deadline, max_deadline), 0, -1):
        if slot[t] is None:
            slot[t] = job_id
            total_profit += profit
            break

print("Profit :", total_profit)
print("Schedule :", slot[1:])