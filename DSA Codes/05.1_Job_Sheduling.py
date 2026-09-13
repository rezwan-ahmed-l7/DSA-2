class Job:
    def __init__(self, profit, deadline, id):
        self.profit = profit
        self.deadline = deadline
        self.id = id

def job_scheduling(profits, deadlines):
    jobs = []
    for index, (p, d) in enumerate(zip(profits, deadlines), start=1):
        jobs.append(Job(p, d, index))

    jobs.sort(key=lambda x: x.profit, reverse=True)

    max_deadline = max(deadlines)
    slot = [None] * (max_deadline + 1)  # Use None instead of 0

    total_profit = 0
    for j in jobs:
        for t in range(min(j.deadline, max_deadline), 0, -1):
            if slot[t] is None:
                slot[t] = j.id
                total_profit += j.profit
                break

    return total_profit, slot[1:]

profits = [25, 15, 30, 20, 12, 35, 5]
deadlines = [4, 3, 4, 2, 1, 3, 2]

total, schedule = job_scheduling(profits, deadlines)

print("Profit :", total)
print("Schedule :", schedule)