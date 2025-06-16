def quickSort(arr1):
    if len(arr1) <= 1:
        return arr1
    else:
        pivot = arr1[0]
        lesser = [i for i in arr1[1:] if i <= pivot]  # Fix: Compare with pivot
        greater = [i for i in arr1[1:] if i > pivot]   # Fix: Compare with pivot
        
        return quickSort(lesser) + [pivot] + quickSort(greater)

print(quickSort([1, 6, 8, 5, 3, 9, 2, 7]))
