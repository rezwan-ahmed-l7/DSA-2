def activity_selection(start, finish):
    n = len(start)

    activities = []
    for i in range(n):
        activities.append((finish[i], start[i], i))

    activities.sort()

    selected = []
    last_finish = -1

    for fin, sta, idx in activities:
        if sta >= last_finish:
            selected.append(idx)
            last_finish = fin

    return selected


start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]

result = activity_selection(start, finish)
print("Selected Activity Index:", result)
