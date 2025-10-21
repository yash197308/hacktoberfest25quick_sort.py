def partition(arr, low, high):
    pivot = arr[low]  # ❌ Wrong pivot
    i = low
    for j in range(low + 1, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[low] = arr[low], arr[i]
    return i

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi)
        quick_sort(arr, pi + 1, high)

arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr))
print(arr)  # Expected [1, 5, 7, 8, 9, 10]
