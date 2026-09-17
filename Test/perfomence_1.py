def sort(a, start, end):

    if start < end:

        mid = (start + end) // 2

        sort(a, start, mid)
        sort(a, mid + 1, end)

        merge(a, start, mid, end)


def merge(a, start, mid, end):

    left = a[start : mid + 1]
    right = a[mid + 1 : end + 1]

    i = j = 0
    k = start

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1

        else:
            a[k] = right[j]
            j += 1
        k += 1

    while i < len(left):

        a[k] = left[i]
        i += 1
        k += 1

    while j < len(right):

        a[k] = right[j]
        j += 1
        k += 1


arr = [2, 1, 4, 3, 8, 5, 6, 9, 7]

sort(arr, 0, len(arr) - 1)

print("Sorted Array:", arr)
