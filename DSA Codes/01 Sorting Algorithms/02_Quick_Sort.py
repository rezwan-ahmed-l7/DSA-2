def partition(arr, start, end):

    pivot = arr[start]
    i = start
    j = end

    while i < j:
        
        while i < end and arr[i] <= pivot:
            i += 1

        while j > start and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[start], arr[j] = arr[j], arr[start]
    return j

def quick_sort(arr, start, end):
    
    if start < end:
        pivot_index = partition(arr, start, end)

        quick_sort(arr, start, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, end)

arr = [10, 16, 8, 12, 15, 6, 3, 9, 5]

quick_sort(arr, 0, len(arr) - 1)
print(arr)