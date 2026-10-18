"""Quick Sort"""


def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


def quicksort(arr, start, end):
    if start < end:
        pivotindex = partition(arr, start, end)
        quicksort(arr, start, pivotindex - 1)
        quicksort(arr, pivotindex + 1, end)


arr = [9, 4, 6, 1, 3, 8, 5, 7, 2]
quicksort(arr, 0, len(arr) - 1)
print(arr)

""" Fractional """

v = [60, 100, 120, 100]
w = [10, 50, 30, 20]
c = 50

item = list(zip(v, w))
item.sort(key=lambda x: x[0] / x[1], reverse=True)

cw = 0
tp = 0.0

for v, w in item:
    if cw + w <= c:
        cw += w
        tp += v
    else:
        rw = c - cw
    f = rw / w
    tp += v * f

print(tp)

""" Job Scheduling """

p = [25, 15, 30, 20, 12, 35, 5]
dl = [4, 3, 4, 2, 1, 3, 2]

jobs = list(zip(p, dl, range(1, len(p) + 1)))
jobs.sort(key=lambda x: x[0], reverse=True)

tp = 0
maxdl = max(dl)
slot = [None] * (maxdl + 1)

for p, dl, jid in jobs:
    for t in range(min(dl, maxdl), 0, -1):
        if slot[t] is None:
            slot[t] = jid
            tp += p
            break

print(tp)
print(slot[1:])

""" Merge Sort """


def sort(arr, start, end):

    if start < end:

        mid = (start + end) // 2

        sort(arr, start, mid)
        sort(arr, mid + 1, end)

        merge(arr, start, mid, end)


def merge(arr, start, mid, end):

    left = arr[start : mid + 1]
    right = arr[mid + 1 : end + 1]

    i = j = 0
    k = start

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):

        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):

        arr[k] = right[j]
        j += 1
        k += 1


arr = [2, 1, 4, 3, 8, 5, 6, 9, 7]

sort(arr, 0, len(arr) - 1)

print("Sorted Array:", arr)
