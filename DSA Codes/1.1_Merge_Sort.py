arr = [2, 1, 4, 3, 8, 5, 6, 9, 7]

def merge_sort(arr, start, end):

    if start < end:

        mid = (start + end) // 2

        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        
        merge(arr, start, mid, end)

def merge(arr, start, mid, end):

    left = arr[start:mid + 1]
    right = arr[mid + 1:end + 1]

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

merge_sort(arr, 0, len(arr) - 1)

print("Sorted Array:", arr)