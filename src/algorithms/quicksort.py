def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    
    left = [x for x in arr if x < pivot]
    mid  = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + mid + quicksort(right)
# implementação básica do algoritmo de ordenação quicksort (o python realmente é bem menor, em C fica enorme)